def freq_palavras(frase):
    '''Função que dados uma frase retorna um dicionario
    contendo quantas vezes a palavra e usada
    ass: str--> dict'''
    ret={}
    a=str.split(frase)
    for i in (a):
        t=a[i]
        ret[t]= str.count(frase, t) 
        
    return ret