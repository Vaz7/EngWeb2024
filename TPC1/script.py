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
        for file_name in file_names:
            tree = ET.parse(f'{folder_path}/{file_name}')
            root = tree.getroot()
            nome_tag = root.find('.//meta/nome')  # Find the <nome> tag inside the <meta> tag
            if nome_tag is not None:
                nome = nome_tag.text
                nomeTrimmed = pattern.sub('',file_name)
                # Do whatever processing you need with the nome value
                indexhtml += f'<li><a href="{nomeTrimmed}.html">{nome}</a></li>'
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
    for casa in root.findall('.//corpo/lista-casas/casa'):
        num = casa.find("número").text
        enfiteuta = casa.find("enfiteuta").text if casa.find("enfiteuta") is not None else ""
        foro = casa.find("foro").text if casa.find("foro") is not None else ""

        html += f'<li>Casa número: {num}</li>'
        html += f'enfiteuta: {enfiteuta}' if enfiteuta else ''
        html += f'<br>'
        html += f'foro: {foro}' if foro else ''

        desc = casa.find('.//desc')
        if desc is not None:
            for para in desc.findall('.//para'):
                # Initialize the text content for the current <para> element
                para_text = ''

                # Handle the text content before the first nested tag (if any)
                if para.text:
                    para_text += f'{para.text.strip()} '

                # Combine the text content with all nested tags in the correct order
                for part in para:
                    if part.tag == 'lugar':
                        para_text += f'<b>{part.text}</b>{part.tail}'
                    elif part.tag == 'entidade':
                        para_text += f'<it>{part.text}</it>{part.tail}'
                    elif part.tag == 'data':
                        para_text += f'<it>{part.text}</it>{part.tail}'

                html += f'<p>{para_text}</p>'
        else:
            html += "<p>No description available.</p>"

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
