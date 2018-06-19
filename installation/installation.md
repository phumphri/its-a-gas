# Installation Guide
## It's a Gas Automotive Sales System
## Summary
These are the instructions for installing "It's a Gas!".  
The architecture consists of three major frameworks.
### Data Acquisition
Several datasources were identified and data downloaded in the form of comma seprated values (CSV) files.
### Data Modeling
Amazon Web Services (AWS) is used to store, model, and provision data.  
The CSV files are stored in the Simple Storage Service (S3).  
These files are loaded into a Postgres database running within the AWS Relational Database Service (RDS).  
Data is modeled using Structured Procedure Language (SQL) and stored procedures.
### Data Access
Data visualization is done with Hypertext Markup Language (HTML) and Javascript.  
These renderings are viewed using a browser such as Google's Chrome.  
Data is provisioned for Javascript through an Application Programming Interface (API) running on Heroku.  
Python programs running on Heroku respond to data requests, make queries to the AWS Postgres database, and return data in a Javascript Object Notation (JSON) format.
## Amazon Web Services
### Create an account on AWS.  
Become familiary with the documentation and tutorials accessed under the Support button.  
Consider subscribing to a Support service to supplement searches on Google.
### Create and Load S3
* Sign into the AWS Console.
* Select the S3 link.
* Create bucket "its-a-gas".
* Select the Permissions tab and then add Everyone with "List objects" as "Yes".
* Modify the CSV files by removing headings, blank lines, and the final newline characters.
* Select the Overview tab.
* Select the Upload button.
* Select the CSV file to upload and then select the Next button.
* In "Manage pulic permissions", select "Grant public read access to this object(s)".
* Select the Upload button.
* Repeat the upload steps for the remaining CSV files.
### Create ACCESS_KEY_ID and SECRET_ACCESS_KEY
Instructions can be found at:
<pre>https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html</pre>
* From the AWS Console, select IAM link.
* Select "Create individual IAM users" button.
* Select "Manage Users" button.
* Select your userid link.
* Select "Create access key" button.
* Save the text file containing ACCESS_KEY_ID and SECRET_ACCESS_KEY.  

In Heroku, environmental variables ACCESS_KEY_ID and SECRET_ACCESS_KEY will be created with these values.
### Create Postgres Database
* From the AWS Console select the "RDS" link.  
* Select "Launch a DB Instance" button in the "Create instance" panel.  
* Click the checkbox "Only enable options eleigible for RDS Free Usage Tier".
* Select the "PostgreSQL" radio button and then select the Next button.  
* Fill in "DB instance identifier" and credentials and select the Next button.
* Make advaced selections and select the "Launch DB instance" button.  
* Int the database, create schema "its_a_gas" under postgres.
* Run the following SQL statements:

<pre> 
CREATE TABLE its_a_gas.domesticautos
(
    month text COLLATE pg_catalog."default" NOT NULL,
    year integer NOT NULL,
    volume double precision NOT NULL,
    combined_volume double precision NOT NULL,
    adjusted_volume double precision NOT NULL,
    sales double precision NOT NULL,
    CONSTRAINT domesticautos_pkey PRIMARY KEY (month, year)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE its_a_gas.domesticautos
    OWNER to postgres;
</pre>

<pre>
CREATE TABLE its_a_gas.foreignautos
(
    month text COLLATE pg_catalog."default" NOT NULL,
    year integer NOT NULL,
    volume double precision NOT NULL,
    combined_volume double precision NOT NULL,
    adjusted_volume double precision NOT NULL,
    sales double precision NOT NULL,
    CONSTRAINT foreignautos_pkey PRIMARY KEY (month, year)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE its_a_gas.foreignautos
    OWNER to postgres;
</pre>

<pre> 
CREATE TABLE its_a_gas.domesticlighttrucks
(
    month text COLLATE pg_catalog."default" NOT NULL,
    year integer NOT NULL,
    volume double precision NOT NULL,
    combined_volume double precision NOT NULL,
    adjusted_volume double precision NOT NULL,
    sales double precision NOT NULL,
    CONSTRAINT domesticlighttrucks_pkey PRIMARY KEY (month, year)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE its_a_gas.domesticlighttrucks
    OWNER to postgres;
</pre>

<pre> 
CREATE TABLE its_a_gas.foreignlighttrucks
(
    month text COLLATE pg_catalog."default" NOT NULL,
    year integer NOT NULL,
    volume double precision NOT NULL,
    combined_volume double precision NOT NULL,
    adjusted_volume double precision NOT NULL,
    sales double precision NOT NULL,
    CONSTRAINT foreignlighttrucks_pkey PRIMARY KEY (month, year)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE its_a_gas.foreignlighttrucks
    OWNER to postgres;
</pre>

<pre> 
CREATE TABLE its_a_gas.manufacturer
(
    model_id text COLLATE pg_catalog."default" NOT NULL,
    model_make_id text COLLATE pg_catalog."default",
    model_name text COLLATE pg_catalog."default",
    model_trim text COLLATE pg_catalog."default",
    model_year text COLLATE pg_catalog."default",
    model_body text COLLATE pg_catalog."default",
    model_engine_position text COLLATE pg_catalog."default",
    model_engine_cc text COLLATE pg_catalog."default",
    model_engine_cyl text COLLATE pg_catalog."default",
    model_engine_type text COLLATE pg_catalog."default",
    model_engine_values_per_cyl text COLLATE pg_catalog."default",
    model_engine_power_ps text COLLATE pg_catalog."default",
    model_engine_power_rpm text COLLATE pg_catalog."default",
    model_engine_torque_nm text COLLATE pg_catalog."default",
    model_engine_torque_rpm text COLLATE pg_catalog."default",
    model_engine_bore_mm text COLLATE pg_catalog."default",
    model_engine_stroke_mm text COLLATE pg_catalog."default",
    model_engine_compression text COLLATE pg_catalog."default",
    model_engline_fuel text COLLATE pg_catalog."default",
    model_top_speed_kph text COLLATE pg_catalog."default",
    model_0_to_100_kph text COLLATE pg_catalog."default",
    model_drive text COLLATE pg_catalog."default",
    model_transmission_type text COLLATE pg_catalog."default",
    model_seats text COLLATE pg_catalog."default",
    model_doors text COLLATE pg_catalog."default",
    model_weight_kg text COLLATE pg_catalog."default",
    model_length_mm text COLLATE pg_catalog."default",
    model_width_mm text COLLATE pg_catalog."default",
    model_height_mm text COLLATE pg_catalog."default",
    model_wheelbase_mm text COLLATE pg_catalog."default",
    model_lkm_hwy text COLLATE pg_catalog."default",
    model_lkm_mixed text COLLATE pg_catalog."default",
    model_lkm_city text COLLATE pg_catalog."default",
    model_fuel_cap_l text COLLATE pg_catalog."default",
    model_sold_in_us text COLLATE pg_catalog."default",
    model_co2 text COLLATE pg_catalog."default",
    model_make_display text COLLATE pg_catalog."default",
    make_display text COLLATE pg_catalog."default",
    make_country text COLLATE pg_catalog."default",
    CONSTRAINT manufacturer_pkey PRIMARY KEY (model_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
</pre>

<pre> 
CREATE TABLE its_a_gas.model_table
(
    model_year integer,
    model_body text COLLATE pg_catalog."default",
    models_offered integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE its_a_gas.model_table
    OWNER to postgres;
</pre>

<pre> 
CREATE TABLE its_a_gas.mpg_table
(
    model_year text COLLATE pg_catalog."default",
    model_make_id text COLLATE pg_catalog."default",
    mpg_city integer,
    mpg_hwy integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE its_a_gas.mpg_table
    OWNER to postgres;
</pre>
<pre> 
CREATE OR REPLACE VIEW its_a_gas.model_view AS
 SELECT model_table.model_year,
    model_table.model_body,
    model_table.models_offered
   FROM its_a_gas.model_table
  ORDER BY model_table.model_year, model_table.models_offered DESC;

ALTER TABLE its_a_gas.model_view
    OWNER TO postgres;

</pre>

<pre> 
CREATE OR REPLACE VIEW its_a_gas.models_offered_by_year AS
 SELECT to_number(manufacturer.model_year, '9999'::text) AS model_year,
    manufacturer.model_body,
    count(manufacturer.model_body) AS models_offered
   FROM its_a_gas.manufacturer
  WHERE manufacturer.model_body IS NOT NULL AND length(manufacturer.model_body) > 0 AND manufacturer.model_body <> '0'::text AND manufacturer.model_body <> 'Not Available'::text AND manufacturer.model_year >= '2000'::text AND manufacturer.model_year <= '2017'::text
  GROUP BY manufacturer.model_year, manufacturer.model_body
  ORDER BY (to_number(manufacturer.model_year, '9999'::text)), (count(manufacturer.model_body)) DESC;

ALTER TABLE its_a_gas.models_offered_by_year
    OWNER TO postgres;
</pre>

<pre> 
CREATE OR REPLACE VIEW its_a_gas.mpg_view AS
 SELECT mpg_table.model_year,
    mpg_table.model_make_id,
    mpg_table.mpg_city,
    mpg_table.mpg_hwy
   FROM its_a_gas.mpg_table
  ORDER BY mpg_table.model_year, mpg_table.model_make_id;

ALTER TABLE its_a_gas.mpg_view
    OWNER TO postgres;
</pre>

<pre> 
CREATE OR REPLACE VIEW its_a_gas.sales_by_year_market_segment AS
 SELECT marketplace.year,
    marketplace.market_segment,
    sum(marketplace.adjusted_volume) AS volume,
    sum(marketplace.sales) AS sales
   FROM ( SELECT domesticautos.year,
            'domestic autos'::text AS market_segment,
            domesticautos.adjusted_volume,
            domesticautos.sales
           FROM its_a_gas.domesticautos
        UNION ALL
         SELECT foreignautos.year,
            'foreign autos'::text AS market_segment,
            foreignautos.adjusted_volume,
            foreignautos.sales
           FROM its_a_gas.foreignautos
        UNION ALL
         SELECT domesticlighttrucks.year,
            'domestic light trucks'::text AS market_segment,
            domesticlighttrucks.adjusted_volume,
            domesticlighttrucks.sales
           FROM its_a_gas.domesticlighttrucks
        UNION ALL
         SELECT foreignlighttrucks.year,
            'foreign light trucks'::text AS market_segment,
            foreignlighttrucks.adjusted_volume,
            foreignlighttrucks.sales
           FROM its_a_gas.foreignlighttrucks
  ORDER BY 1, 2) marketplace
  WHERE marketplace.year >= 2000 AND marketplace.year <= 2017
  GROUP BY ROLLUP(marketplace.year, marketplace.market_segment)
  ORDER BY marketplace.year, marketplace.market_segment;

ALTER TABLE its_a_gas.sales_by_year_market_segment
    OWNER TO postgres;
</pre>

<pre> 
CREATE OR REPLACE VIEW its_a_gas.sales_rollup AS
 SELECT sales_by_year_market_segment.year,
    COALESCE(sales_by_year_market_segment.market_segment, 'total'::text) AS market_segment,
    sales_by_year_market_segment.volume,
    sales_by_year_market_segment.sales
   FROM its_a_gas.sales_by_year_market_segment;

ALTER TABLE its_a_gas.sales_rollup
    OWNER TO postgres;
</pre>

<pre> 
CREATE OR REPLACE FUNCTION its_a_gas.build_model_table(
	)
    RETURNS void
    LANGUAGE 'sql'

    COST 100
    VOLATILE 
AS $BODY$

delete from its_a_gas.model_table;
	
insert into its_a_gas.model_table
select *
from its_a_gas.models_offered_by_year;

CREATE or replace VIEW its_a_gas.model_view AS
 SELECT *
   FROM its_a_gas.model_table
  ORDER BY model_table.model_year, model_table.models_offered DESC;

ALTER TABLE its_a_gas.model_table
    OWNER TO postgres;

ALTER TABLE its_a_gas.model_view
    OWNER TO postgres;
	
ALTER FUNCTION its_a_gas.build_model_table()
    OWNER TO postgres;

$BODY$;

ALTER FUNCTION its_a_gas.build_model_table()
    OWNER TO postgres;
</pre>

You will be creating a "Config Var" on Heroku called "AWS_POSTGRES".  Use the credentials entered.  
A sample value would look like this:  
<pre>host=postgres.cx7bhejrlrq0.us-east-2.rds.amazonaws.com dbname=postgres user=postgres password=postgres</pre>
## Heroku
* Select the menun icon.
* Select the Dashboard link.
* Select the New listbox.
* Select "Create new app" item.
* Enter your name for the fapplication into "App name".
* Select "Create app" button.
* Select the "GitHub, Connect to GitHub" icon.
* Enter the name of the GitHub repository in the lisbox and select the Search button.
* Select the Connect button.
* Select the "Enable Automatic Deploys" button.
* Select Settings link.
* Select "Reveal Confg Vars" button.
* Add environmental variable ACCESS_KEY_ID and assign the value from AWS.
* Add environmental variable SECRET_ACCESS_KEY and assign the value from AWS.
* Add environmental variable AWS_POSTGRES and assign the connection string from AWS.
* Add environmental variable LOCAL_POSTGRES.  This is not used in Heroku but is expected by the programs.
* Select "Add buildpack".
* Select "python" icon.
* Select "Save changes".
* Select "Resources" link.
* Select "refresh master" button to pull in "Procfile" and "requirements.txt" files from GitHub.
* Select Overview tab to observe the build.
## Load Data
Prefixed with the newly created Heroku app, run the following API calls using Postman:
* /data_loader/domesticautos
* /data_loader/foreignautos
* /data_loader/domesticlighttruccks
* /data_loader/foreignlighttrucks
* /manufacturer_loader
* /build_model_table  

Validate the load by running the following API calls using Postman:
* /manufacturer
* /domesticautos
* /foreignautos
* /domesticlighttrucks
* /foreignlighttrucks
* /sales_rollup
* /models_offered_by_year
* /mpg
* /gdp  

Fix all errors.  When there is a clean load, open Chrome pointing to the Heroku prefix for the newly created application.
