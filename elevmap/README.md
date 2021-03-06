     ___________________________________________________
    |  _____                       _____ _ _       _    |
    | |  __ \                     |  __ (_) |     | |   |
    | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
    | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
    | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
    | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
    |                   __/ |                           |
    |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
    |___________________________________________________|


Elevation Map Service
=====================

- subscribes to socket "gps" (lat, lon) and publishes corresponding elevation data based on SRTM elevation data.
- please download the corresponding SRTM files from: [http://dds.cr.usgs.gov/srtm/version2_1/SRTM3](http://dds.cr.usgs.gov/srtm/version2_1/SRTM3) and put them into the "service" folder.
- an example file for the area I live in is provided: N50E010.hgt.

This software uses GDAL, which is a translator library for raster and vector geospatial data formats.
