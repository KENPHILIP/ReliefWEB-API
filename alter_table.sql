select * from dtm_file_contents c join dtm_file_metadata m
on c.metadata_id = m.id;

select distinct Country_name from dtm_file_metadata;

Alter table dtm_file_metadata
ADD column Region_code Varchar(255);

Alter table dtm_file_metadata
add column Admin_level Varchar(255); 

Alter table dtm_file_metadata
add column Country_ISO3_code Varchar(255);

Alter table dtm_file_metadata
add column Country_name Varchar(255);

Alter table dtm_file_metadata
add column region Varchar(255);

Alter table dtm_file_metadata
add column survey_date date;

Alter table dtm_file_metadata
add column Round Varchar(255);

Alter table dtm_file_metadata
add column site_name Varchar(255);

Alter table dtm_file_metadata
add column Sub_county Varchar(255);

Alter table dtm_file_metadata
add column DataType Varchar(255);

Alter table dtm_file_metadata
add column URLLINK Varchar(255);

Alter table dtm_file_metadata
add column purpose Varchar(255);

ALTER TABLE dtm_file_metadata
DROP COLUMN Region_code,
DROP COLUMN Admin_level,
DROP COLUMN Country_ISO3_code,
DROP COLUMN Country_name,
DROP COLUMN region,
DROP COLUMN survey_date,
DROP COLUMN Round,
DROP COLUMN site_name,
DROP COLUMN Sub_county;

--locust table
Alter table locust
add column DataType Varchar(255);


