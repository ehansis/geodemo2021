from functools import partial
from pathlib import Path
import json

from owslib.wms import WebMapService
from shapely.geometry import shape, box
from shapely.ops import transform
import pyproj


data_dir = Path(__file__).parent / "data"


def get_wms_map(wms_url, boundary, layer_name, resolution_m=25):
    """
    Query image from Copernicus WMS service

    Args:
        wms_url (str): WMS URL
        boundary (shape): boundary of map to query (image is queried for bbox of this shape)
        layer_name (str): layer name to query
        resolution_m (int): resolution to query at, in m

    Returns:
        bytes: binary image data
    """

    # extract bounding box, reproject to EPSG 3857 (in meters, same coords as CLC raster maps)
    # reprojection follows example in https://shapely.readthedocs.io/en/stable/manual.html#shapely.ops.transform
    project = partial(
        pyproj.transform,
        pyproj.Proj("epsg:4326"),
        pyproj.Proj("epsg:3857"),
        always_xy=True,
    )
    bbox = transform(project, box(*boundary.bounds))

    # compute number of pixels at desired resolution
    width = round((bbox.bounds[2] - bbox.bounds[0]) / resolution_m)
    height = round((bbox.bounds[3] - bbox.bounds[1]) / resolution_m)

    wms = WebMapService(wms_url)

    # query the image as tiff, write to a temporary file
    i = wms.getmap(
        layers=[layer_name],
        styles=["default"],
        srs="EPSG:3857",
        bbox=bbox.bounds,
        size=(width, height),
        format="image/tiff",
    ).read()

    return i


if __name__ == "__main__":

    # load munich boundary from GeoJSON, convert to Shapely shape
    munich_geojson = json.load((data_dir / "munich.json").open())
    munich = shape(munich_geojson["features"][0]["geometry"])

    # To get the names of queryable layers: open (for example)
    # https://copernicus.discomap.eea.europa.eu/arcgis/services/GioLandPublic/HRL_TreeCoverDensity_2018/ImageServer/WMSServer?request=GetCapabilities&service=WMS
    # and view the XML source; there are three (sub-)layers with attribute "queryable = 1".
    # Those can be queried by name.

    maps = [
        (
            "tree_cover_density",
            "https://image.discomap.eea.europa.eu/arcgis/services/GioLandPublic/HRL_TreeCoverDensity_2018/ImageServer/"
            "WMSServer?request=GetCapabilities&service=WMS",
            "HRL_TreeCoverDensity_2018:None",
            25,
        ),
        (
            "grassland",
            "https://image.discomap.eea.europa.eu/arcgis/services/GioLandPublic/HRL_Grassland_2018/ImageServer/"
            "WMSServer?request=GetCapabilities&service=WMS",
            "HRL_Grassland_2018:None",
            25,
        ),
        (
            "small_woody_features",
            "https://image.discomap.eea.europa.eu/arcgis/services/GioLandPublic/HRL_SmallWoodyFeatures_2015_005m/"
            "ImageServer/WMSServer?request=GetCapabilities&service=WMS",
            "0",
            27,
        ),
    ]

    for file_name, url, layer, res in maps:
        img = get_wms_map(url, munich, layer, resolution_m=res)
        with open(data_dir / f"{file_name}_{res}.tiff", "wb") as f:
            f.write(img)
