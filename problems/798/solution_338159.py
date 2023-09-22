def freq_palavras(frases):
    '''Função que dados uma frase retorna um dicionario
    contendo quantas vezes a palavra e usada
    ass: str--> dict'''
    ret={}
    a=str.split(frases)
    i=0
    while i<len(a):
        
    	ret[a[i]]= list.count(a, a[i])
        i=i+1
    return ret