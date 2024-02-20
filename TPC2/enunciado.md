
# Enunciado TPC2

- Processar o dataset do mapa virtual.
- Criar uma página para cada cidade: c1.html.c2.html, etc...
- Página principal com os nomes de todas as cidades, cada cidade é um link do tipo: 
<a> href="http://localhost:7777/c3"> Braga </a> 
- Serviço em node: 
  / => responde com a página principal
  /c1 => responde com a página da cidade c1
- Na página da cidade:
  -nome,id,distrito,população.
  -ligações com partida da cidade: nome da cidade e ao clicar faz um pedido para a página dessa cidade
