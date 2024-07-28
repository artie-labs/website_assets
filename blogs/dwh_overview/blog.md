Your data warehouse is the central location of all analytics processes, so it is important that you choose the right one. Whether you are building out your data stack from scratch, or looking to replace your current warehouse, we will walk you through the pros and cons of Snowflake vs Redshift vs BigQuery vs ClickHouse. 

## Factors to consider

Before we jump into the different data warehouse options, it’s important to look at the most important qualities when it comes to deciding on a warehouse. 

**Price**

You need to understand how each warehouse calculates costs so that you choose one that will allow you to stick within your budget. Some warehouses are known for running up costs when not properly managed, making it vital to do your research on how to keep these at bay. Choosing a data warehouse with a cost-management plan in place can help you feel confident about your decision. 

**Speed**

You want your queries to be performant so you don’t need to constantly babysit them. A slow data warehouse is an analytics and data engineer’s worst nightmare! We always recommend trialing different products and testing some of your most complex queries to see how they perform. 

**Security**

Data warehouses need to meet the security standards your company has in place for its data, ensuring its safety at rest and in transit. Pay close attention to how your data is handled, especially if working with healthcare or financial data. You don’t want any surprises here! 

**Engineering experience required**

Someone on your team will need to closely manage your data warehouses for things like cost management, performance, and security. Some warehouses are more complex than others, so make sure you have someone on your team who can handle their complexities. While experience with data warehouses in general is preferred, it can help to have someone with previous experience working with the exact warehouse you choose. 

**Team use cases**

Can the data warehouse handle the use cases you throw at it? Some warehouses are better for analytics while others are made to handle machine learning and data science. Make sure a data warehouse has all of the capabilities you need before landing on a decision. Again, test these out in the trial period! 

## Snowflake

![Snowflake](snowflake.png)

[Snowflake](https://www.snowflake.com/en/) is a flexible data warehouse that enables data storage and processing with a strong focus on analytics. It focuses on **ease of use**, automating maintenance tasks that other warehouses do not.

Snowflake has extensive JSON support, offering native functions that make querying denormalized data a breeze. It also allows for easy data sharing between accounts, which can be helpful for larger enterprise companies with multiple lines of business.

Snowflake offers flexibility in pricing tiers, allowing you to pay for only the features that you need. However, they charge based on usage, leading costs to grow as you scale. The auto clustering service can quickly eat up costs due to low visibility, making it sometimes necessary to build cost-management tools alongside Snowflake. It’s also imperative to closely monitor your warehouse size, choosing one just small enough to perform well. 

## Redshift

![Redshift](redshift.png)

[Redshift](https://aws.amazon.com/redshift/) is a fast, scalable data warehouse part of the Amazon Web Services (AWS) suite of products. It offers bundled computing and storage which allows for scalability (but not necessarily flexibility). Redshift contains customizable encryption solutions that can be tailored to fit your needs, making its security top-notch. Because it is an AWS product, it integrates seamlessly with other AWS tools.

Unlike Snowflake, Redshift is not as easy to use and requires hands-on maintenance such as vacuuming (other than vacuum deletes) and compression, two processes that can’t be automated. It requires you to plan sort and dist keys for optimal performance.

It also lacks built-in functions, especially for handling JSON, which makes it difficult to work with at times. For example, I recently followed [this tutorial](https://www.getdbt.com/blog/how-to-unnest-arrays-in-redshift) from dbt on how to unnest arrays in Redshift due to the lack of internal support. These are just a few examples of why Redshift better suits a team of more experienced engineers. 

## BigQuery

![BigQuery](bigquery.png)

[BigQuery](https://cloud.google.com/bigquery) is a serverless, cost-effective data warehouse solution built by Google. Because it is serverless, you don’t have to worry about supporting any infrastructure. It is also quite scalable, automatically scaling resources up and down as needed.

BigQuery supports SQL, Python, R, and other ETL processing all in one platform. Because of this, it is more tailored towards data science and machine learning use cases rather than SQL analytics. If this is something you are looking for in a data warehouse, this can be a huge benefit.

While BigQuery is generally less expensive, they charge on bytes processed, making unoptimized queries heavier on the pockets. This can lead to unexpected costs if not careful with the code you are running. For this reason, it may work best with a team of more experienced analytics engineers. 

## ClickHouse

![Clickhouse](clickhouse.png)

[ClickHouse](https://clickhouse.com/) is a column-oriented database management system made for online analytical processing (OLAP). It can process hundreds of millions to over a billion rows and tens of gigabytes of data by a single server in just a second with its use of table engines. The query performance is lightning speed due to data being sorted, indexed, and compressed into columns. This also makes it ideal for large batch updates.

However, ClickHouse tends to underperform with smaller batch updates, making it less than ideal for those with low data volume. It also lacks the ability to modify or delete data as a regular process, making this a manual process for the user.

ClickHouse tends to be more of a Postgres alternative than a data warehouse alternative. It also uses a dialect of SQL rather than SQL itself, giving it more of a learning curve for any data engineer. Make sure your team is comfortable with this before deciding to go with ClickHouse. 

## Conclusion

When considering any of these data warehouses, you need to consider price, speed, security, available engineering experience, and team use cases. The data warehouse that is best for you, and that you ultimately decide on, will be determined by your needs.

* If you have a small team of mainly data analysts, Snowflake may be your best option.
* If you have a larger team of senior data engineers, Redshift could work for you.
* Or maybe your team has both analytics and data science use cases. Then BigQuery may best suit your needs.
* If you have lots of web event data that needs to be stored, ClickHouse could serve this purpose well.

No matter which data warehouse you choose, Artie is here to help sync all your data from your database to your data warehouse in real time. 
