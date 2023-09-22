def freq_palavras(frase):
    '''Função que dados uma frase retorna um dicionario
    contendo quantas vezes a palavra e usada
    ass: str--> dict'''
    ret={a[0]:1}
    a=str.split(frase)
    for i in (a):
        ret[a[i+1]]= str.count(frase, a[i]) 
        
    return ret