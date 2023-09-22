def freq_palavras(frases):
    '''	Dado uma string, a função deve retornar um dicionário onde cada palavra dessa string seja
    uma chave e tenha como valor o número de vezes que essa palavra aparece;
    str-> dict'''
    i=0
    t=1
    z=0
    
    lista=[]
    
    for i in count(frases,''):
        if frase[i:t]=='':
            lista=lista + frase[z:t]
            z=+t    
        else:
            i=+1
            t=+1
            
    dicio={}
    p=0
    f=1
    while p<len(lista):
        if (lista[p] not in dicio) and (lista[f] not in dicio):
            dicio=+{lista[p]:count(lista,lista[p]),lista[f]:count(lista,lista[f])}
            p=+1
            f=+1