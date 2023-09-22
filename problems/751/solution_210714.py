# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    frase = str.split(frase)
    for d in frase:
        frase = list.count(frase, d)
    return frase