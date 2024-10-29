CREATE EXTENSION postgis

--The error "Geometry has M dimension but column does not" indicates that the geometries you are trying to insert have both Z (3D) and M (measure) dimensions, but your geom column only allows 3D geometries (Z dimension) without the M dimension.

--To handle geometries with both Z and M dimensions (XYZM), you need to update the geom column to allow geometries with both Z and M dimensions. You can modify the column to use POINTZM (or GEOMETRYZM if you are unsure about the specific geometry type) to accommodate both dimensions.
--Notes:
--geom column: The GEOMETRY(Geometry, 4326) part assumes that your spatial data uses the WGS 84 coordinate system (EPSG:4326). Adjust this according to your spatial reference system.
--Data Types: The data types (e.g., FLOAT, VARCHAR, DATE, etc.) were inferred from the column names. Ensure that they fit the data you will be inserting.

ALTER TABLE locust 
    ALTER COLUMN geom TYPE GEOMETRY(POINTZM, 4326); -- Change to POINTZM or GEOMETRYZM for both Z and M dimensions
--

-- Insert swarm_master data
INSERT INTO locust (locust_type, geom)
SELECT 'swarm', geom
FROM swarm_master;

-- Insert band_master data
INSERT INTO locust (locust_type, geom)
SELECT 'band', geom
FROM band_master;

-- Insert hopper_master data
INSERT INTO locust (locust_type, geom)
SELECT 'hopper', geom
FROM hopper_master;

--4. Verify the combined data:
SELECT locust_type, ST_AsText(geom) 
FROM locust;
