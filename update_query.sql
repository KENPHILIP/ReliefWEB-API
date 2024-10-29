ALTER TABLE public.dtm_file_metadata
ADD COLUMN URL_link VARCHAR(255);
ADD COLUMN purpose VARCHAR(255) ;

UPDATE public.dtm_file_metadata
SET URL_link = 'https://dtm.iom.int/datasets', purpose = 'Displacement Tracking Matrix (DTM) datasets for monitoring population movements.';


ALTER TABLE floodobservatory_api_dat
ADD COLUMN URL_link VARCHAR(255),
ADD COLUMN purpose VARCHAR(255) ;

UPDATE floodobservatory_api_dat
SET URL_link =  'https://floodobservatory.colorado.edu/temp/FloodArchive.xlsx', purpose = 'Flood Observatory Archive for historical flood data and impact analysis.';

ALTER TABLE glidenumber_api
ADD COLUMN URL_link VARCHAR(255),
ADD COLUMN purpose VARCHAR(255) ;

UPDATE glidenumber_api
SET URL_link = 'https://www.glidenumber.net/glide/public/search/search.jsp', purpose = 'Glide Number Search for global disaster event tracking and information.';


ALTER TABLE icpac_disasters
ADD COLUMN URL_link VARCHAR(255),
ADD COLUMN purpose VARCHAR(255) ;

UPDATE icpac_disasters
SET URL_link = 'https://sedac.ciesin.columbia.edu/data/set/pend-gdis-1960-2018', purpose = 'Global Disaster Impact and Exposure Data from 1960 to 2018.';
