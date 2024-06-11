Sleeping Duck, an online mattress retailer, improved data freshness and increased business operations efficiency for their Customer Experience, Finance, Marketing, and Supply Chain teams by adopting Artie.

> Since adopting Artie, we have seen a fourfold increase in the frequency of key business data updates without additional costs. This enhancement has allowed all departments, including Customer Experience, Finance, Marketing, and Supply Chain, to access more current information on their dashboards.
>
> <cite>-- Chao Li, Senior Data Engineer at Sleeping Duck</cite>

# Key Takeaways

1. Sleeping Duck had time-of-day requirements for data freshness and wanted a solution where data latency of their core production data could be configured. As their business needs change over time, they wanted a solution that could enable real-time data for certain critical tables.
2. Artie offered a plug-and-play solution that solves their data latency needs and eliminates the need for any day to day maintenance.
3. With Artie, the company has seen a fourfold increase in the frequency of key business data updates without any additional computational costs. With the ability to provide real-time data replication, Artie helps future proof Sleeping Duck’s data platform.

![img_3.png](img_3.png)

## Sleeping Duck wanted to adjust data latency based on time-of-day business needs

Sleeping Duck is a retail company that designs, manufactures, and sells mattresses online. Core business and application data including sales transactions, inventory metrics, and website functionality logs are stored in their Postgres database. The data engineering team then transfers data to Snowflake to run analytics and power core business operations, which include monitoring website performance, predicting inventory needs, and managing warehouse logistics workflows.

Previously, Sleeping Duck used a batched ETL solution from a SaaS provider for their Postgres to Snowflake data replication. Observed data latency was ~1 hour which was not ideal for operational use cases. Chao Li, Senior Data Engineer at Sleeping Duck, wanted a better solution that was not only faster but offered the flexibility to enable real-time syncs on critical tables. He evaluated several solutions, including Fivetran, Stitch, Matillion, and Datorios, but none were as easy as Artie to set up. Most alternate solutions did not provide the level of support he wanted and required hands-on maintenance, which was not ideal for his small team of engineers.

## Sleeping Duck chose Artie for its data latency flexibility and Eco Mode functionality

> Working with Artie was exceptionally positive. Their genuine attentiveness to our needs distinguished them from other vendors. The onboarding process was smooth and the team promptly addressed any issues that came up.

Sleeping Duck chose Artie for database replication for several key reasons:

* Artie **reduced data latency from 1 hour to 15 minutes**, a four-fold increase in critical business data updates without an increase in Snowflake compute costs. Importantly, Artie offered the ability to stream data in real-time, which helps future proof the needs of the business as new use cases come up.
* [Artie’s Eco Mode](https://www.artie.so/blogs/snowflake-eco-mode) provides the ability to adjust replication frequency based on time-of-day demands. Sleeping Duck mostly leverages 15 minute syncs during peak business hours and 6 hour syncs outside of business hours when data analysts/engineers are not utilizing the data. **This feature helped reduce Snowflake ingestion costs by 51%!**
* Plug and play solution. The **ease of implementation and zero maintenance requirements** was a big factor in choosing Artie. In addition, the [Analytics Portal](https://www.artie.so/blogs/introducing-arties-analytics-portal) provides unparalleled visibility into usage and latency. The monitors on database and data pipeline health also helps Sleeping Duck’s data team proactively manage issues.
* Robust technical support. The Artie team’s genuine attentiveness to customer’s technical needs and ability to go above and beyond to help solve customer’s problems.

## Future proofing their data platform with Artie

Timely data is vital for making accurate business and logistical decisions, especially for an ecommerce business. For Sleeping Duck, the Postgres to Snowflake connector is crucial as it drives their core business operations. Many departments, including Customer Experience, Finance, Marketing, and Supply Chain teams leverage production data for daily business workflows.

> Artie has become an indispensable tool for us. Alternatives might exist, but they would likely result in increased costs and a diminished user experience, as data dashboard refresh rates across teams would be slower.

As Sleeping Duck’s business evolves and their data freshness requirements change, the team is confident that Artie is the best tool to future proof their data infrastructure.

<br/><br/>

**About Artie**: Artie is a real time data replication solution for databases and data warehouses. Artie leverages change data capture (CDC) and stream processing to perform data syncs in a more efficient way, which enables sub-minute latency and helps optimize compute costs. With Artie, any company can set up streaming pipelines in minutes without coding.

**About Sleeping Duck**: [Sleeping Duck](https://www.sleepingduck.com/) is a company based in Melbourne, Australia that designs, manufactures, and retails mattresses online. The company has won multiple awards and is the world’s first fully customisable mattress. 
