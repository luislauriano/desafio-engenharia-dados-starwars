import re

def clean_numeric(value):
    if value in ["unknown", "n/a", "none"] or value is None:
        return None
    
    try:
        cleaned = re.sub(r'[^0-9.]', '', str(value))
        return float(cleaned) if cleaned else None
    except (ValueError, TypeError):
        return None

def transform_person(p):
    return {
        "name": p["name"],
        "height": clean_numeric(p["height"]),
        "mass": clean_numeric(p["mass"]),
        "birth_year": p["birth_year"],
        "gender": p["gender"],
        "url": p["url"],
        "films_count": len(p.get("films", []))
    }

def transform_planet(p):
    return {
        "name": p["name"],
        "climate": p["climate"],
        "terrain": p["terrain"],
        "surface_water": clean_numeric(p["surface_water"]),
        "population": clean_numeric(p["population"]),
        "url": p["url"]
    }

def transform_starship(s):
    return {
        "name": s["name"],
        "model": s["model"],
        "max_atmosphering_speed": clean_numeric(s["max_atmosphering_speed"]),
        "hyperdrive_rating": clean_numeric(s["hyperdrive_rating"]),
        "url": s["url"]
    }

def transform_film(f):
    return {
        "title": f["title"],
        "episode_id": f["episode_id"],
        "release_date": f["release_date"], 
        "url": f["url"]
    }