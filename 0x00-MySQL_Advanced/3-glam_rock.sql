-- list all bands with Glam rock as their main style

SELECT
    band_name,
    IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock'
ORDER BY longevity DESC;
