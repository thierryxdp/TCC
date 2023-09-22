# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Da à quantidade de palavras em uma frase;
     str -> int'''
      palavras = str.split (frase)
      palavras = list (palavras)
      palavras = len (palavras)
      return palavras