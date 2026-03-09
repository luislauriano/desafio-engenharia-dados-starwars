from data_pipeline.extract import fetch_data
from data_pipeline.transform import transform_person, transform_planet, transform_starship, transform_film
from data_pipeline.load import insert_people, insert_starships, insert_planets, insert_films

def run_pipeline():
    print("Iniciando pipeline de dados SWAPI...")
    
    people = fetch_data("people")
    if people:
        people = [transform_person(p) for p in people] 
        success = insert_people(people) 
        if success:
            print("Carga de people executada com sucesso!")
        else:
            print("Falha na carga de people.")
    else:
        print("Falha na extração de people.")
    
    planets = fetch_data("planets")
    if planets:
        planets = [transform_planet(p) for p in planets]
        success = insert_planets(planets) 
        if success:
            print("Carga de planets executada com sucesso!")
        else:
            print("Falha na carga de planets.")
    else:
        print("Falha na extração de planets.")
    
    starships = fetch_data("starships")
    if starships:
        starships = [transform_starship(s) for s in starships]
        success = insert_starships(starships) 
        if success:
            print("Carga de starships executada com sucesso!")
        else:
            print("Falha na carga de starships.")
    else:
        print("Falha na extração de starships.")
    
    films = fetch_data("films")
    if films:
        films = [transform_film(s) for s in films]
        success = insert_films(films) 
        if success:
            print("Carga de starships executada com sucesso!")
        else:
            print("Falha na carga de filmes.")
    else:
        print("Falha na extração de filmes.")
    
   

if __name__ == "__main__":
    run_pipeline()