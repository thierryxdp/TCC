# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq(texto):
    '''Dado um texto, retorna um dicionário onde cada palavra
    desse texto é uma chave e tem como valor o número de vezes
    que a palavra aparece. str -> dict'''
    T=str.split(texto)
    d={}
    for palavra in T:
        if palavra not in d:
            d[palavra]= 1
        else:
            d[palavra]+=1
    return d