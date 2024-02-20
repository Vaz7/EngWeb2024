import json
import re
import os

porta = 7777


def createIndexPage():
    indexhtml = html = """
        <!DOCTYPE html>
        <html lang="pt-PT">
        <head>
            <title>Ruas </title>
            <meta charset="utf-8">
            <link rel = "stylesheet" href="my.css"/>
        </head>
        <body>
        <div class="list">
        <ul>
        """
    
    with open('mapa-virtual.json', 'r') as file:
        # Parse JSON data
        parsed_data = json.load(file)

    for city in parsed_data['cidades']:
        indexhtml += f'<li><a href="http://localhost:{porta}/{city["id"]}">{city["nome"]}</a></li>'
    indexhtml += '</body></html></ul></div><div class="animation"></div>'

    with open("html/index.html", "w", encoding="utf-8") as output_file:
        output_file.write(indexhtml)

def createCityPages():
    with open('mapa-virtual.json', 'r') as file:
        # Parse JSON data
        parsed_data = json.load(file)

    # Iterate over each city and add its name to the list
    for city in parsed_data['cidades']:
        html = """
    <!DOCTYPE html>
    <html lang="pt-PT">
    <head>
        <meta charset="utf-8">
        <link rel = "stylesheet" href="my.css"/>
    
    """
        html += f'<title>{city["nome"]}</title>'
        html += f'</head><body>'
        html += f'<a href="http://localhost:{porta}/" class="button">Home</a>'
        html += f'<h1>{city["nome"]}</h1>'
        html += f'<br>'
        html += f'<h4>População: {city["população"]}</h4>'
        html += f'<br>'
        html += f'<div class="text"><h4>Descrição: {city["descrição"]}</h4></div>'
        html += f'<br>'
        html += f'<h4>Distrito: {city["distrito"]}</h4>'
        html += "<br>"
        html += f'<b>Ligações a partir de {city["nome"]}:</b>'
        html += f'<div class="list"><ul>'
        for ligacao in parsed_data['ligacoes']:
            if ligacao["origem"] == city["id"]:
                for cidade in parsed_data['cidades']:
                    if cidade["id"] == ligacao["destino"]:
                        html += f'<li><a href="http://localhost:{porta}/{cidade["id"]}">{cidade["nome"]}</a></li>'
        
        
        html += '</body></ul></div><div class="animation"></div></html>'

        with open(f'html/{city["id"]}.html', "w", encoding="utf-8") as output_file:
            output_file.write(html)

def main():
    createIndexPage()
    
    createCityPages()


if __name__ == '__main__':
    main()