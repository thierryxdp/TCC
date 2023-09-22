def freq_palavras(a):
    'recebe uma string e retorna um dicionario com o numero de vezes que a palavra repete'
    'entrada: str'
    'saida: dicio'
    lista=str.split(a,' ')
    dicio={}
    for x in lista:
        dicio[x]= list.count(lista,x)
    return dicio