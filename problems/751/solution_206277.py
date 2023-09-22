# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    "Retorna o número de palavras da frase. str->int"
    f = str.split(frase," ")
    return len(f)