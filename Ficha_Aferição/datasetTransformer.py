import json

def transform_json(json_data):
    transformed_data = {}
    for person in json_data:
        for desporto in person['desportos']:
            if desporto not in transformed_data:
                transformed_data[desporto] = []
            transformed_data[desporto].append(person['_id'])
    return [{"nome": desporto, "pessoas": pessoas} for desporto, pessoas in transformed_data.items()]

# Path to the input JSON file
input_file_path = "datasets/dataset.json"

# Path to the output JSON file
output_file_path = "datasets/datasetDesp.json"

# Reading JSON data from the input file with UTF-8 encoding
with open(input_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Transforming the JSON data
transformed_data = transform_json(json_data)

# Writing the transformed data to the output file with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as file:
    for entry in transformed_data:
        json.dump(entry, file, ensure_ascii=False)
        file.write('\n')

print("Transformation completed. Transformed data has been written to", output_file_path)
