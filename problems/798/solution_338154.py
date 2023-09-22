def freq_palavras(frases):
    '''Função que dados uma frase retorna um dicionario
    contendo quantas vezes a palavra e usada
    ass: str--> dict'''
    ret={}
    a=str.split(frases)
    ret[a[0]]= str.count(frases, a[0])