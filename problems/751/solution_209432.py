# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def conta_palavras(frase):
    """função que dada uma frase retorna o numero de PALAVRAS da frase sem contar o
espaço entre elas str->int"""
    return len(str.split(frase))