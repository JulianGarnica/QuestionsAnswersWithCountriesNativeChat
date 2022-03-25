from csv import reader
import json 

file_name = "plantilla.csv"
estructureJSON = {}

with open(file_name, "r") as csv_file:
    csv_reader = reader(csv_file, delimiter = ",") # Important
    header = next(csv_reader)

    for row in csv_reader:
      estructureJSON[row[0]] = {
        "type": "goal",
        "display-name": row[0],
        "steps": [
          {
            "conditions": [
              "{{$not paisSeleccionado}}"
            ],
            "type": "conversation",
            "conversation": "welcome"
          }
        ]
      }
      for i in range(1,len(row)):
        estructureObject = {
          "conditions": [
            "{{$eq paisSeleccionado '%s'}}" % (header[i])
          ],
          "type": "message",
          "messages": [
            row[i]
          ]
        }
        estructureJSON[row[0]]["steps"].append(estructureObject)
      estructureJSON[row[0]]["steps"].append(
        {
          "type": "command",
          "command": "invalidate-entity respondioPregunta"
        }
      )

      estructureJSON[row[0]]["steps"].append(
        {
          "type": "command",
          "command": "invalidate-entity calificacionSeleccionada"
        }
      )

      estructureJSON[row[0]]["steps"].append(
        {
          "type": "command",
          "command": "go-to \xC2\xBFRespond\xC3\xAD tu duda?"
        }
      )
 
json_string = json.dumps(estructureJSON, indent = 4, ensure_ascii=False).encode('utf8')
json = json_string.decode()
archi1=open("resultado.json","w")
archi1.write(json)
archi1.close()