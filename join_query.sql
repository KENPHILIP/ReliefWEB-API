SELECT * FROM glidenumber_api g JOIN icpac_disasters i
ON g.country_code = i.iso3;

select * from dtm_file_contents c join dtm_file_metadata m
on c.metadata_id = m.id;

SELECT * FROM DTM_file_metadata WHERE file_extension = '.xlsx';

SELECT * FROM DTM_file_view;

SELECT fc.file_contents, fm.file_name
FROM DTM_file_metadata fm
JOIN DTM_file_contents fc ON fm.id = fc.metadata_id
WHERE fm.file_extension = '.xlsx';

select d.metadata_id, d.file_contents from public.dtm_file_contents d join
public.dtm_file_metadata dt on d.id=dt.id;

select * from public.dtm_file_metadata ;

select distinct file_path from public.dtm_file_metadata;
select distinct file_reference from public.country_files;

select * from public.swarm_master;

select c.country_name, s.startdate, s.finishdate, s.countryid from public.swarm_master s 
join public.country c on c.country_code = s.countryid;

select i.country, g.country_code, i.geolocation from public.icpac_disasters i join
public.glidenumber_api g on i.country = g.country;

