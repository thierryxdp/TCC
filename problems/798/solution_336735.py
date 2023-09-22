# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras (frases):
    """Função que recebe uma string e retorna um
    dicionário com todas as palavras do string com a
    quantidade de vezes que cada uma aparece
    str -> dic"""
    lista = str.split(frases)
    dicio = {}
    for p in lista:
        dicio[p] = list.count(lista, p)
    return dicio