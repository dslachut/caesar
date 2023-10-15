import json
from functools import lru_cache
from importlib import resources

import dash_leaflet.express as dlx

from caesar import data


@lru_cache(maxsize=1)
def ar_crops():
    hexen_json = [json.loads(l) for l in resources.read_text(data, "ar_crops.jsonl").splitlines()]
    for i, obj in enumerate(hexen_json):
        hexen_json[i]["properties"][
            "tooltip"
        ] = f"{obj['properties']['crop_name']}, {obj['properties']['elev_range']:.2f}m elev chg"
        hexen_json[i]["properties"]["color"] = obj["properties"]["crop_color"][:-2]
        # if hexen_json[i]["properties"]["name"] == "Woody Wetlands":
        #    hexen_json[i]["properties"]["icon"] = "forestwetlands.png"
    return {"type": "FeatureCollection", "features": hexen_json}
