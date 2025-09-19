# A better way to handle Postgres partitioned tables for CDC

Partitioned tables are common in Postgres, but it's often a headache when it comes to trying to replicate that data.

Here are some challenges that companies run into:

1. Are the partitions following a particular regex pattern?
2. Are the partitions stored in a separate schema from the actual table?
3. Are the partitioned tables stored in the publication?
4. The desire to fan all of these partitions into a single table downstream
5. A regular table changed to a partitioned table and breaking downstream dependencies

Fortunately, you are able to create a publication in Postgres with `publish_via_partition_root` that makes these problems easier to deal with.

```sql
CREATE PUBLICATION my_pub FOR ALL TABLES WITH (publish_via_partition_root = true);
```

> What does `publish_via_partition_root` do?

This means that all the incoming CDC messages for each of the partitions will be instead published with the root table name as opposed to the partition name.

### Are the partitions following a particular regex pattern?

> First off, why do we care?

There are a couple of reasons why we need to understand the layout:

1. We'll need to know this if we're fanning partitions into a single topic
2. We'll need to know this to know whether we should process or ignore this when we see this CDC message.

For the most part, most companies follow some sort of layout like:

* {{tableName}}_YYYY_MM
* {{tableName}}_default

And if this were the case, we can easily solve this with a regular expression pattern like this: `{{tableName}}_((default)|([0-9]{4})_(0[1-9]|1[012]))$`

> What if your layout was less deterministic?

What if you weren't partitioning your table based on timestamp and instead was partitioning off a region identifier?

For example, if the partitions were something like `orders_sf`, `orders_oakland`, and there is a non-partitioned table called `orders_total`. By creating too wide of a regular expression, we may accidentally match on the non-partitioned table. However, if it was too narrow, then we risk not picking up new partitions. This process then becomes error prone, but also labourous.

By using `publish_via_partition_root`, users will no longer need to specify a regular expression as there is no need to include the actual partitions as we only care about the root table.

