import json

# Read data from the JSON file
with open("filmes.json", "r") as file:
    data = json.load(file)

# Extract id and designacao from each occurrence
atoresEmFilmes = {}

for entry in data["filmes"]:
    cast = entry.get("cast", [])  # Default to an empty list if 'genres' key is not found
    for ator in cast:
        filmeID = entry.get("id")
        if ator in atoresEmFilmes:
            atoresEmFilmes[ator].append(filmeID+ ":" + entry.get("title"))
        else:
            atoresEmFilmes[ator] = []
            atoresEmFilmes[ator].append(filmeID+ ":" + entry.get("title"))

total_entries = len(atoresEmFilmes)
current_entry = 0

# Write each item in the dictionary as a separate entry in the JSON file
with open("atores.json", 'w') as json_file:
    json_file.write('{"atores":[')
    for key, value in atoresEmFilmes.items():
        entry = {key: value}
        json.dump(entry, json_file)
        
        # Check if it's not the last entry, then add a comma
        if current_entry < total_entries - 1:
            json_file.write(',')
        
        json_file.write('\n')  # Add a newline between entries
        current_entry += 1
    json_file.write(']}')