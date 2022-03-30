from csv import reader
import json 

file_name = "PlantillaCSVImportaciónPreguntas.csv"
maxPreguntas = 50
diferentesArchivos = []
estructureJSON = []

with open(file_name, "r", encoding="utf8") as csv_file:
    csv_reader = reader(csv_file, delimiter = ";") # Important
    header = next(csv_reader)

    cont = 0
    for row in csv_reader:

      # if cont == maxPreguntas-1:        
      #   diferentesArchivos.append(estructureJSON)
      #   cont = 0
      #   estructureJSON = []
      # else:
      if(row[0] == ""):
        value = "default "+ str(cont)
      else:
        value = row[0] + str(cont)
      estructureJSON.append({
        "value": value,
        "expressions": [row[1]],
        "answers": [row[2]]
      })
      cont += 1

totalPreguntas = cont

json_string = json.dumps(estructureJSON[200:214], ensure_ascii=False).encode('utf8')
json = json_string.decode()
#print(json)
archivo = f"resultadoEstructuraRara4.json"
archi1=open(archivo,"w", encoding='utf-8')
archi1.write(json)
archi1.close()
cont += 1