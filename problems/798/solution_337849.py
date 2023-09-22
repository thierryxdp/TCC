# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    ''' função que recebe uma string e retorna um dicionário
    com a quantidade de cada palavra da string
    str -> dict
    '''
    palavras = frase.split()
    dict1 = {}
    i = 0
    for elementos in palavras:
        dict1[palavras[i]] = palavras.count(palavras[i])
        i += 1
    return dict1