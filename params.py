def params(response):
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    r2 = toponym["boundedBy"]["Envelope"]
    low = ','.join(r2["lowerCorner"].split())
    up = ','.join(r2["upperCorner"].split())
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "bbox": "~".join([low, up]),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude, "comma"])
    }
    return map_params
