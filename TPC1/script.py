import os
import re
import xml.etree.ElementTree as ET



def list_files_in_folder(folder_path):
    file_list = []
    try:
        # Get all file names in the specified folder
        files = os.listdir(folder_path)

        # Add each file name to the list
        for file_name in files:
            file_list.append(file_name)

        return file_list

    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")
        return None


def buildIndexPage():
    indexhtml = html = """
        <!DOCTYPE html>
        <html lang="pt-PT">
        <head>
            <title>Ruas </title>
            <meta charset="utf-8">
        </head>
        <body>
        """

    #remover os prefixos e extensoes de ficheiros
    pattern = re.compile(r'^MRB-\d{2}-|\.xml$')

    folder_path = './MapaRuas-materialBase/texto'  # Replace with the actual path to your folder
    file_names = list_files_in_folder(folder_path)

    if file_names is not None:
        file_names_without_prefix = [pattern.sub('', name) for name in file_names]
        for file_name in file_names_without_prefix:
            indexhtml += f'<li><a href="{file_name}.html">{file_name}</a></li>'
    indexhtml += '</body></html>'

    with open("html/index.html", "w", encoding="utf-8") as output_file:
        output_file.write(indexhtml)
    return file_names

def buildContentPage(rua):
    folder_path = './MapaRuas-materialBase/texto'
    pattern = re.compile(r'^MRB-\d{2}-|\.xml$')
    ruaTrimmed = pattern.sub('', rua)

    html = """
    <!DOCTYPE html>
    <html lang="pt-PT">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
    """


    xml_file_path = f'{folder_path}/{rua}'
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    numero = root.find('.//meta/número').text
    nome = root.find('.//meta/nome').text

    html += f'Número da rua: {numero}'
    html += f'<br>'
    html += f'Nome da rua: {nome}'




    #escrever texto descritivo da rua
    for para in root.findall('.//corpo/para'):
        # Combine the text content before <lugar> with the wrapped <a> tags
        para_text = ''.join([
            para.text or '',
            ''.join([f'<b>{lugar.text}</b>{lugar.tail}' for lugar in para.findall('lugar')]),
            ''.join([f'<it>{entidade.text}</it>{entidade.tail}' for entidade in para.findall('entidade')]),
        ])

        html += f'<p>'
        html += f'{para_text}'
        html+= f'</p>'



    #meter figuras
    for figura in root.findall('.//corpo/figura'):
        path_without_dots = re.sub(r'^\.\./', '', figura.find("imagem").attrib["path"])
        fig="<figure>"
        fig += f'<img src="../MapaRuas-materialBase/{path_without_dots}"style="width:50%">'
        fig+=f'<figcaption>{figura.find('legenda').text}</figcaption></figure>'

        html += fig

    html += "<ul>"



    #as casas ainda nao esta direito

    #escrever casas
    for casa in root.findall('.//lista-casas/casa'):
        num = casa.find("número")
        enfiteuta = casa.find("enfiteuta")
        foro = casa.find("foro")
        html += f'<li>Casa número: {num.text}</li>'
        html += f'enfiteuta: {enfiteuta.text}' if enfiteuta is not None else ''
        html += f'<br>'
        html += f'foro: {foro.text}' if foro is not None else ''

        desc = casa.find('.//desc')
        if desc is not None:
            if desc.find('para') is not None:
                print(desc.find('para').text)
            text = ''.join([
                para.text or '',
                ''.join([f'<b>{data.text}</b>{data.tail}' for data in desc.findall('.//data')]),
                ''.join([f'<b>{lugar.text}</b>{lugar.tail}' for lugar in para.findall('.//lugar')]),
            ])
            html += f'<p>{text}</p>'

    html += "</ul>"












    html += '</body></html>'

    with open(f'html/{ruaTrimmed}.html', "w", encoding="utf-8") as output_file:
        output_file.write(html)



def main():
    listRuas = buildIndexPage()


    for rua in listRuas:
        buildContentPage(rua)



if __name__ == '__main__':
    main()
