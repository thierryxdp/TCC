def freq_palavras(frases):
    '''Dado uma string, a função deve retornar um dicionário 
    onde cada palavra dessa string seja uma chave e tenha como
    valor o número de vezes que essa palavra aparece;
    str ->dict'''
    lista = str.split(frases)
    
    dicionario={}
    p=0 
    while p<=len(lista):
        dicionario[p]=(list.count(lista,p))
        p=+1
    
    return (dicionario)