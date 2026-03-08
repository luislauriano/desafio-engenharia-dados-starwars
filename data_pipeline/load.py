from data_pipeline.db_connection import get_connection

def insert_people(people_list):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(f"Iniciando a carga de {len(people_list)} registros em 'people'...")
        for p in people_list:
            cursor.execute(
                """
                INSERT INTO people (name, height, mass, birth_year, gender, url, films_count)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING;
                """,
                (p["name"], p["height"], p["mass"], p["birth_year"], p["gender"], p["url"], p["films_count"])
            )
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao inserir pessoas: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def insert_planets(planets_list):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(f"Iniciando a carga de {len(planets_list)} registros em 'planets'...")
        for p in planets_list:
            cursor.execute(
                """
                INSERT INTO planets (name, climate, terrain, surface_water, population, url)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING;
                """,
                (p["name"], p["climate"], p["terrain"], p["surface_water"], p["population"], p["url"])
            )
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao inserir planetas: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def insert_starships(starships_list):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(f"Iniciando a carga de {len(starships_list)} registros em 'starships'...")
        for s in starships_list:
            cursor.execute(
                """
                INSERT INTO starships (name, model, max_atmosphering_speed, hyperdrive_rating, url)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING;
                """,
                (s["name"], s["model"], s["max_atmosphering_speed"], s["hyperdrive_rating"], s["url"])
            )
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao inserir naves: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def insert_films(films_list):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(f"Iniciando a carga de {len(films_list)} filmes...")
        for f in films_list:
            cursor.execute(
                """
                INSERT INTO films (title, episode_id, release_date, url)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING;
                """,
                (f["title"], f["episode_id"], f["release_date"], f["url"])
            )
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao inserir filmes: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()