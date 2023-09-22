# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    "dada uma frase, retorna o ńumero de palavras da frase. str->int"
    sem_espaco = str.strip(frase)
    qtd = sem_espaco.count(" ")
    return qtd+1