CREATE TABLE DTM_IOM_datasets (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255),
    file_path TEXT,
    file_extension VARCHAR(10),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    file_contents BYTEA  -- Use BYTEA to store binary data if needed (e.g., for small files)
);


CREATE TABLE FloodObservatory_API_DAT (
    ID SERIAL PRIMARY KEY,
    GlideNumber VARCHAR(50),
    Country VARCHAR(100),
    OtherCountry VARCHAR(100),
    long FLOAT,
    lat FLOAT,
    Area VARCHAR(255),
    Began DATE,
    Ended DATE,
    Validation BOOLEAN,
    Dead INT,
    Displaced INT,
    MainCause VARCHAR(255),
    Severity VARCHAR(50)
);


CREATE TABLE glidenumber_API (
    id SERIAL PRIMARY KEY,  -- Auto-incrementing primary key
    GLIDE_number VARCHAR(50),
    Event VARCHAR(255),
    Country VARCHAR(100),
    Date_ DATE, 
    Event_Code VARCHAR(50),
    Glide_Serial VARCHAR(50),
    Country_Code VARCHAR(10),
    Year INT,
    Month INT,
    Day INT,
    Source VARCHAR(255),
    Comments TEXT,
    Latitude FLOAT,
    Longitude FLOAT,
    Created TIMESTAMP,  -- Stores the timestamp when the record was created
    Updated TIMESTAMP,  -- Stores the timestamp when the record was last updated
    Location VARCHAR(255),
    Magnitude FLOAT
);



CREATE TABLE icpac_disasters (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100),
    iso3 VARCHAR(3),
    gwno INT,
    year INT,
    geo_id VARCHAR(50),
    geolocation TEXT,
    level VARCHAR(50),
    adm1 VARCHAR(255),
    adm2 VARCHAR(255),
    adm3 VARCHAR(255),
    location VARCHAR(255),
    historical BOOLEAN,
    hist_country VARCHAR(100),
    disastertype VARCHAR(100),
    disasterno VARCHAR(50),
    latitude FLOAT,
    longitude FLOAT
);


   CREATE TABLE "EM_DAT" (
    DisNo VARCHAR(255) PRIMARY KEY,
    Historic TEXT,
    Classification_Key TEXT,
    Disaster_group TEXT,
    Disaster_Subgroup TEXT,
    Disaster_Type TEXT,
    Disaster_Subtype TEXT,
    External_IDs TEXT,
    Event_Name TEXT,
    ISO TEXT,
    Country TEXT,
    Subregion TEXT,
    Region TEXT,
    Location TEXT,
    Origin TEXT,
    Associated_Types TEXT,
    OFDA_BHA_Response TEXT,
    Appeal TEXT,
    Declaration TEXT,
    AID_Contribution NUMERIC,
    Magnitude NUMERIC,
    Magnitude_Scale TEXT,
    Latitude NUMERIC,
    Longitude NUMERIC,
    River_Basin TEXT,
    Start_Year NUMERIC,    -- Changed from BIGINT to NUMERIC
    Start_Month INTEGER,
    Start_Day INTEGER,
    End_Year NUMERIC,      -- Changed from BIGINT to NUMERIC
    End_Month INTEGER,
    End_Day INTEGER,
    Total_Deaths NUMERIC, -- Changed from BIGINT to NUMERIC
    No_Injured NUMERIC,   -- Changed from BIGINT to NUMERIC
    No_Affected NUMERIC,  -- Changed from BIGINT to NUMERIC
    No_Homeless NUMERIC,  -- Changed from BIGINT to NUMERIC
    Total_Affected NUMERIC, -- Changed from BIGINT to NUMERIC
    Reconstruction_Costs NUMERIC,
    Reconstruction_Costs_Adjusted NUMERIC,
    Insured_Damage NUMERIC,
    Insured_Damage_Adjusted NUMERIC,
    Total_Damage NUMERIC,
    Total_Damage_Adjusted NUMERIC,
    CPI NUMERIC,
    Admin_Units TEXT,
    Entry_Date DATE,
    Last_Update DATE
);



create extension postgis;

SELECT * FROM public."EM_DAT"
WHERE "disno" IN ('2024-0509-ETH', '2024-0541-ETH', '2024-0544-SDN', '2024-0588-UGA');


SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'EM_DAT';

SELECT * FROM public."EM_DAT";
select distinct insured_damage from public."EM_DAT";





