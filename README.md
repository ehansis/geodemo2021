# geodemo2021
Demo content for GeoMob Munich Meetup, July 2021

_Scripted, testable, scalable, and free! - A tour of geospatial analysis in Python_

## Demo content

The presentation slides are defined in [slides.md](https://github.com/ehansis/geodemo2021/blob/main/slides.md), you
can view all the content there, including links to references.
The pretty, htlm-ified slides are in `slides.html`. 
You'd need to clone the repo (or download that file) to view them.

The blueprint for the live demo is in `pre_recorded_demo.ipynb`.
You can view the notebook without dowloading it in [nbviewer](https://nbviewer.jupyter.org/github/ehansis/geodemo2021/blob/main/pre_recorded_demo.ipynb).


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


## Raster data queries (land cover)

The example raster data used in the demo is part of the [Copernicus High Resolution Layers](https://land.copernicus.eu/pan-european/high-resolution-layers) dataset.
Code for downloading the relevant data is in `clc_raster_query.py`.

Please refer to the Copernicus website for further information, in particular concering [Terms of Use](https://land.copernicus.eu/terms-of-use).


## Python environment

This demo was created using [Conda](https://conda.io/) to build and manage the Python environment.
You can re-create the environment by [installing conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
and running
```
conda env create -f conda_env.yml -n geodemo2021
```


## Slide compilation

Slides are defined in `slides.md`. Compile them to html with
```
pandoc -t revealjs -V theme=moon -s slides.md -o slides.html
```

