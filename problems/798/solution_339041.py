def freq_palavras(frases):
    '''	Dado uma string, a função deve retornar um dicionário onde cada palavra dessa string seja
    uma chave e tenha como valor o número de vezes que essa palavra aparece;
    str-> dict'''
    lista= str.split(frases)
           
    dicio={}
    p=0
    f=1
    while p<len(lista):
        if (lista[p] not in dicio) and (lista[f] not in dicio):
            dicio=dicio+{lista[p]:list.count(lista,lista[p]),lista[f]:list.count(lista,lista[f])}
            p=+1
            f=+1