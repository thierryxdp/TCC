# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
 def conta_palavras(frase):
    #frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)