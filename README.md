# geodemo2021
Demo content for GeoMob Munich Meetup, July 2021

_Scripted, testable, scalable, and free! - A tour of geospatial analysis in Python_


## Grid data preproc

* load Tiffs, inspect
* Convert to binary masks  
* interpolate where necesary
* AND them together, convert to int


## Vector data preproc

* buffer
* unary_union -> single multipolygo
* explode -> many polys, but attributes are lost
* label exploded polys
* sjoin with original dataset, how=right to keep group label
* groupy.first to keep one entry per group label


## Voronoi zonal stats

https://github.com/WZBSocialScienceCenter/geovoronoi

https://regionmask.readthedocs.io/en/stable/


## OpenStreetMap data queries

School data and Munich city boundaries were queried from OpenStreetMap via [Overpass Turbo](http://overpass-turbo.eu)
and exported from there as GeoJSON.

Data are ©[OpenStreetMap](https://www.openstreetmap.org/copyright) under [ODbL](https://opendatacommons.org/licenses/odbl/).

The query for `data/schools.json` was:
```
[out:json][timeout:60];
{{geocodeArea:Munich}}->.searchArea;
(
  node["amenity"="school"]["name"~"[Gg]rundschule"](area.searchArea);
  way["amenity"="school"]["name"~"[Gg]rundschule"](area.searchArea);
  relation["amenity"="school"]["name"~"[Gg]rundschule"](area.searchArea);
);
out body;
>;
out skel qt;
```

The query for `data/munich.json` was:
```
[out:json][timeout:60];
(
  relation["de:amtlicher_gemeindeschluessel"="09162000"];
);
out body;
>;
out skel qt;
```


## Python environment

This demo was created using [Conda](https://conda.io/) to build and manage the Python environment.
You can re-create the environment by [installing conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
and running
```
conda env create -f conda_env.yml
```


## Slides

Slides are defined in `slides.md`. Compile them to html with
```
pandoc -t revealjs -V theme=moon -s slides.md -o slides.html
```

