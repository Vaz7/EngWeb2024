import json

# Read data from the JSON file
with open("filmes.json", "r") as file:
    data = json.load(file)

# Extract id and designacao from each occurrence
filmesEmGeneros = {}

for entry in data["filmes"]:
    genres = entry.get("genres", [])  # Default to an empty list if 'genres' key is not found
    for genero in genres:
        filmeID = entry.get("id")
        
        if genero in filmesEmGeneros:
            filmesEmGeneros[genero].append(filmeID+ ":" + entry.get("title"))
        else:
            filmesEmGeneros[genero] = []
            filmesEmGeneros[genero].append(filmeID+ ":" + entry.get("title"))

total_entries = len(filmesEmGeneros)
current_entry = 0

# Write each item in the dictionary as a separate entry in the JSON file
with open("generos.json", 'w') as json_file:
    
    json_file.write('"generos":[')
    for key, value in filmesEmGeneros.items():
        entry = {key: value}
        json.dump(entry, json_file)
        
        # Check if it's not the last entry, then add a comma
        if current_entry < total_entries - 1:
            json_file.write(',')
        
        json_file.write('\n')  # Add a newline between entries
        current_entry += 1
    json_file.write(']}')

     
