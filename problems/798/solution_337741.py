def freq_palavras(frase):
    '''a funcao retorna um dicionario, a chave é uma palavra da frase e o valor quantas vezes se repete
    str->dict'''
    d=dict()
    frase=frase.split(' ')
    for i in frase:
        if i not in d:
            d[i]=1
        else: 
            d[i]+=1
    return d