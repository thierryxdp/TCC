# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(x):
    '''Essa função retorna o número de vezes que aparece cada palavra de uma frase
    str -> dict'''
    lista_palavras = x.split()
    dicionario = dict.fromkeys(lista_palavras,0)
    for contador in range(len(lista_palavras)):
        dicionario[lista_palavras[contador]] += 1
    return dicionario