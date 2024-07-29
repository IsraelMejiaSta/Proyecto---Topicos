import csv
import json

with open("C:\\Users\\israe\\Downloads\\listado_ferti_excluidos22-tlax.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["NUMERO"],row["ESTADO"],row["MUNICIPIO"],row["NOMBRE"])

f = open("C:\\Users\\israe\\Downloads\\datos.json", encoding="utf8")
data = json.load(f)
for i in data:
    print(i)
f.close()


## crar un archivo csv
with open("C:\\Users\\israe\\Downloads\\usuario.csv",mode ="w",encoding="utf8") as csvfile:
    fieldname = ["user","municipio","numero"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({"user":"israel","municipio":"israel","numero":"69"})


## crear un archivo json
dictionary = [{"user":"israel","apellido":"mejia","municipio":"metepec"},
              {"user":"theshit","apellido":"lalo","municipio":"xona"}]
json_object = json.dumps(dictionary, ident=2)
with open("C:\\Users\\israe\\Downloads\\usuariojson.json",mode ="w",encoding="utf8") as json_file:
    json_file.writelines(json_object)