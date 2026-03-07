from data_pipeline.extract import fetch_data
from data_pipeline.load import insert_people

def run_pipeline():
    print("Iniciando pipeline de dados SWAPI...")
    
    people = fetch_data("people")
    
    if people:
        success = insert_people(people) 
        if success:
            print("Pipeline executada com sucesso!")
        else:
            print("Pipeline falhou durante a fase de carga.")
    else:
        print("Falha na extração: nenhum dado encontrado.")

if __name__ == "__main__":
    run_pipeline()