from data_pipeline.db_connection import get_connection

def clean_numeric(value):
    if value in ["unknown", "n/a", "none"]:
        return None
    try:
        return value.replace(",", "")
    except AttributeError:
        return value

def insert_people(people_list):
    conn = get_connection()
    cursor = conn.cursor()

    print(f"Iniciando a carga de {len(people_list)} registros no banco...")

    try:
        for p in people_list:
            cursor.execute(
                """
                INSERT INTO people (name, height, mass, birth_year, gender, url, films_count)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING;
                """,
                (
                    p["name"],
                    clean_numeric(p["height"]),
                    clean_numeric(p["mass"]),
                    p["birth_year"],
                    p["gender"],
                    p["url"],
                    len(p["films"])
                )
            )
        
        conn.commit()
        print("Carga finalizada com sucesso!")
        
    except Exception as e:
        print(f"Erro durante a carga: {e}")
        conn.rollback() 
    finally:
        cursor.close()
        conn.close()