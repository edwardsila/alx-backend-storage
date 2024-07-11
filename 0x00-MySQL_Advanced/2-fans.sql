-- ranks country origins of bands

SOURCE /root/alx-backend-storage/0x00-MySQL_Advanced/metal_bands.sql

CREATE VIEW temporary AS
SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin;

-- now select from the temporary table
SELECT
    origin,
    nb_fans
FROM
    temporary
ORDER BY
    nb_fans DESC;
