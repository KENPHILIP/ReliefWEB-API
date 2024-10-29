-- Metadata Table for Viewing
CREATE TABLE DTM_file_metadata (
    id SERIAL PRIMARY KEY,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_extension TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- File Contents Table
CREATE TABLE DTM_file_contents (
    id SERIAL PRIMARY KEY,
    metadata_id INTEGER REFERENCES DTM_file_metadata(id) ON DELETE CASCADE,
    file_contents BYTEA
);

-- Creating a View to Combine Metadata and File Contents
CREATE VIEW DTM_file_view AS
SELECT 
    fm.id AS file_id,
    fm.file_name,
    fm.file_path,
    fm.file_extension,
    fm.upload_date,
    fc.file_contents
FROM 
    DTM_file_metadata fm
LEFT JOIN 
    DTM_file_contents fc
ON 
    fm.id = fc.metadata_id;
	

CREATE TABLE DTM_IOM_datasets (
    id SERIAL PRIMARY KEY,
    url_link TEXT,
    purpose TEXT,
    file_name TEXT,
    file_path TEXT,
    file_extension TEXT,
    file_contents BYTEA
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
    Date_ DATE,  -- The underscore in 'Date_' is used to avoid conflicts with the reserved keyword 'Date'
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

CREATE TABLE locust (
    LOCUSTID SERIAL PRIMARY KEY,
    locust_type VARCHAR(50),
    geom GEOMETRY(GeometryZ, 4326), -- Accepts 3D geometry (X, Y, Z) with SRID 4326
    STARTDATE DATE,
    TmSTARTDAT TIME,
    FINISHDATE DATE,
    TmFINISHDA TIME,
    EXACTDATE DATE,
    PARTMONTH VARCHAR(50),
    LOCNAME VARCHAR(255),
    AREAHA FLOAT,
    LOCRELIAB VARCHAR(255),
    COUNTRYID VARCHAR(50),
    REPORTID VARCHAR(50),
    ACOMMENT TEXT,
    LOCPRESENT FLOAT,
    SPECIESQRY FLOAT,
    CONFIRMATN FLOAT,
    BREEDING FLOAT,
    REPRELIAB FLOAT,
    SHPMINDSQM FLOAT,
    SHPMAXDSQM FLOAT,
    SHPMINDSIT FLOAT,
    SHPMAXDSIT FLOAT,
    SHPDENISOL FLOAT,
    SHPDENSCAT FLOAT,
    SHPDENGRP FLOAT,
    SHPDENUNK FLOAT,
    SHPSC FLOAT,
    SHPSCCAT FLOAT,
    SHPMATEGG FLOAT,
    SHPMATHAT FLOAT,
    SHPMATINS1 FLOAT,
    SHPMATINS2 FLOAT,
    SHPMATINS3 FLOAT,
    SHPMATINS4 FLOAT,
    SHPMATINS5 FLOAT,
    SHPMATINS6 FLOAT,
    SHPMATFLED FLOAT,
    SHPMATUNK FLOAT,
    SHPCOLGN FLOAT,
    SHPCOLGNYL FLOAT,
    SHPCOLGNBK FLOAT,
    SHPCOLYLBK FLOAT,
    SHPCOLBK FLOAT,
    SHPAPPSOL FLOAT,
    SHPAPPTRAN FLOAT,
    SHPAPPGREG FLOAT,
    SHPAPPUNK FLOAT,
    GHPMINDSQM FLOAT,
    GHPMAXDSQM FLOAT,
    GHPMINDSIT FLOAT,
    GHPMAXDSIT FLOAT,
    GHPDENLOW FLOAT,
    GHPDENMED FLOAT,
    GHPDENHI FLOAT,
    GHPDENUNK FLOAT,
    GHPSC FLOAT,
    GHPSCCAT FLOAT,
    GHPMATEGG FLOAT,
    GHPMATHAT FLOAT,
    GHPMATINS1 FLOAT,
    GHPMATINS2 FLOAT,
    GHPMATINS3 FLOAT,
    GHPMATINS4 FLOAT,
    GHPMATINS5 FLOAT,
    GHPMATINS6 FLOAT,
    GHPMATFLED FLOAT,
    GHPMATUNK FLOAT,
    GHPCOLGN FLOAT,
    GHPCOLYLBK FLOAT,
    GHPCOLBK FLOAT
);
