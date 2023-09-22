# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os
     parâmetros de entrada e saída"""
  palavras = str.split(frase)
  list.reverse(palavras)
  espaco = " "
  return str.join(espaco, palavras)