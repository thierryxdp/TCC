# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    "Retorne o numero de palavras de uma dada frase; str->int"
    x=len(frase)
    y=len(str.split(frase))
    return y