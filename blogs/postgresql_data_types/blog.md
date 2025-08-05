# PostgreSQL Data Types: A Complete Guide to Vanilla PostgreSQL

When you're building data pipelines or designing database schemas, understanding PostgreSQL data types is crucial. The wrong data type choice can lead to performance issues, storage waste, or even data integrity problems. But with PostgreSQL's rich type system, it's easy to get overwhelmed by the options.

Most teams start with basic types like `VARCHAR` and `INTEGER`, but they miss out on PostgreSQL's powerful built-in types that can make their applications more robust and efficient. They end up with oversized columns, poor performance, and maintenance headaches.

At Artie, we believe that choosing the right data type is fundamental to building reliable data infrastructure. PostgreSQL's type system is one of its greatest strengths—it provides both safety and flexibility. Understanding these types helps you make informed decisions about your data model, whether you're building applications or setting up CDC pipelines.

## Numeric Types

### Integer Types

**SMALLINT** (2 bytes)
- Range: -32,768 to +32,767
- Use case: Small numbers like ages, counts, or status codes
```sql
CREATE TABLE users (
    age SMALLINT,
    status_code SMALLINT DEFAULT 1
);
```

**INTEGER/INT** (4 bytes)
- Range: -2,147,483,648 to +2,147,483,647
- Use case: Most common integer type for IDs, counts, and general numbers
```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1
);
```

**BIGINT** (8 bytes)
- Range: -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807
- Use case: Large numbers like timestamps, very large counts, or when you need the maximum range
```sql
CREATE TABLE events (
    id BIGINT PRIMARY KEY,
    timestamp BIGINT,
    user_count BIGINT
);
```

### Decimal Types

**DECIMAL/NUMERIC** (variable)
- Precision and scale: DECIMAL(p,s) where p is total digits, s is decimal places
- Use case: Financial data, measurements requiring exact precision
```sql
CREATE TABLE transactions (
    amount DECIMAL(10,2),
    tax_rate DECIMAL(5,4)
);
```

**REAL** (4 bytes)
- 6 decimal digits precision
- Use case: Scientific calculations, approximate values
```sql
CREATE TABLE measurements (
    temperature REAL,
    pressure REAL
);
```

**DOUBLE PRECISION** (8 bytes)
- 15 decimal digits precision
- Use case: High-precision scientific calculations
```sql
CREATE TABLE scientific_data (
    pi_value DOUBLE PRECISION,
    gravity DOUBLE PRECISION
);
```

## Character Types

**CHAR(n)** (fixed length)
- Fixed-length character string, padded with spaces
- Use case: Codes, identifiers with known length
```sql
CREATE TABLE products (
    sku CHAR(10),
    country_code CHAR(2)
);
```

**VARCHAR(n)** (variable length)
- Variable-length character string with maximum length
- Use case: Most common text type for names, descriptions, variable content
```sql
CREATE TABLE users (
    name VARCHAR(100),
    email VARCHAR(255),
    bio VARCHAR(1000)
);
```

**TEXT** (variable length)
- Unlimited length character string
- Use case: Long text content, when you don't want to specify a limit
```sql
CREATE TABLE articles (
    title VARCHAR(200),
    content TEXT,
    comments TEXT
);
```

## Date and Time Types

**DATE** (4 bytes)
- Date only (no time component)
- Range: 4713 BC to 5874897 AD
- Use case: Birth dates, event dates, calendar dates
```sql
CREATE TABLE events (
    event_date DATE,
    birth_date DATE
);
```

**TIME** (8 bytes)
- Time of day only
- Use case: Store time without date context
```sql
CREATE TABLE schedules (
    start_time TIME,
    end_time TIME
);
```

**TIMESTAMP** (8 bytes)
- Date and time without timezone
- Use case: Local timestamps, when timezone doesn't matter
```sql
CREATE TABLE logs (
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);
```

**TIMESTAMPTZ** (8 bytes)
- Date and time with timezone
- Use case: Applications with users in different timezones
```sql
CREATE TABLE global_events (
    scheduled_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**INTERVAL** (16 bytes)
- Time span or duration
- Use case: Durations, time calculations
```sql
CREATE TABLE subscriptions (
    duration INTERVAL,
    trial_period INTERVAL DEFAULT '30 days'
);
```

## Boolean Type

**BOOLEAN** (1 byte)
- True, false, or null
- Use case: Flags, status indicators, yes/no data
```sql
CREATE TABLE users (
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    premium_member BOOLEAN
);
```

## Binary Data Types

**BYTEA** (variable length)
- Binary data (byte array)
- Use case: File uploads, binary content, encrypted data
```sql
CREATE TABLE files (
    file_data BYTEA,
    thumbnail BYTEA
);
```

## Geometric Types

**POINT** (16 bytes)
- Geometric point (x,y)
- Use case: GPS coordinates, 2D positions
```sql
CREATE TABLE locations (
    coordinates POINT,
    address VARCHAR(255)
);
```

**LINE** (32 bytes)
- Infinite line
- Use case: Mathematical applications, graphics
```sql
CREATE TABLE drawings (
    line_segment LINE
);
```

**CIRCLE** (24 bytes)
- Circle with center and radius
- Use case: Geographic boundaries, mathematical shapes
```sql
CREATE TABLE zones (
    coverage_area CIRCLE
);
```

## Network Address Types

**INET** (7 or 19 bytes)
- IPv4 or IPv6 host address
- Use case: IP addresses, network applications
```sql
CREATE TABLE connections (
    ip_address INET,
    user_agent VARCHAR(255)
);
```

**CIDR** (7 or 19 bytes)
- IPv4 or IPv6 network address
- Use case: Network ranges, subnet masks
```sql
CREATE TABLE networks (
    subnet CIDR,
    description VARCHAR(100)
);
```

**MACADDR** (6 bytes)
- MAC address
- Use case: Network hardware identification
```sql
CREATE TABLE devices (
    mac_address MACADDR,
    device_name VARCHAR(100)
);
```

## JSON Types

**JSON** (variable length)
- JSON data (stored as text)
- Use case: Flexible schema, API responses
```sql
CREATE TABLE api_logs (
    request_body JSON,
    response_data JSON
);
```

**JSONB** (variable length)
- Binary JSON (more efficient)
- Use case: JSON data with indexing and querying needs
```sql
CREATE TABLE user_profiles (
    preferences JSONB,
    metadata JSONB
);
```

## Array Types

PostgreSQL allows arrays of any data type:
```sql
CREATE TABLE products (
    tags TEXT[],
    prices DECIMAL(10,2)[],
    colors VARCHAR(50)[]
);
```

## Key Takeaways

1. **Choose the smallest type that fits your data**: Use SMALLINT instead of INTEGER when possible, VARCHAR(n) instead of TEXT for bounded strings.

2. **Consider timezone requirements**: Use TIMESTAMPTZ for global applications, TIMESTAMP for local-only data.

3. **Use JSONB over JSON**: JSONB is more efficient and supports indexing and complex queries.

4. **Leverage PostgreSQL's rich type system**: Don't just use VARCHAR for everything—PostgreSQL has specialized types for specific use cases.

5. **Think about storage and performance**: Smaller types use less storage and can be faster to process.

## Design Principles

- **Type safety first**: Let PostgreSQL's type system catch errors early
- **Storage efficiency**: Choose types that minimize storage while maintaining functionality
- **Query performance**: Consider how your data types affect indexing and query performance
- **Future-proofing**: Consider how your data might grow or change over time

PostgreSQL's type system is one of its most powerful features. By understanding and using the right types for your data, you can build more robust, efficient, and maintainable applications. Whether you're building a simple web app or setting up complex data pipelines, the right data type choices will pay dividends in performance and reliability.

Ready to dive deeper into PostgreSQL's advanced features? Check out our [guide to logical replication](link-to-logical-replication-blog) or explore how we handle [schema evolution in CDC pipelines](link-to-schema-blog).
