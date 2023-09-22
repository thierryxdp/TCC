def freq_palavras(frases):
    '''a funcao reconhece uma frase e retorna um dicionário que cataloga a frequencia de cada palavra
       str->dicionário'''
    dicionario={}
    f=str.split(frases)
    i=0
    while i<len(f):
        lista=list.count(f,f[i])
        dic[f[i]]=lista
        i=i+1
    return dic