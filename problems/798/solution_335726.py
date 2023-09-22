def freq_palavras (frases):
    '''funcao que retorna um dicionario com uma chave contendo o numero de repeticoes que uma palavra tem na frase inserida.'''
    '''str=>dic'''
   
    dic={}
    n=1
    lista=str.split(frases)
    for p in lista:
        if p in dic:
            dic[p]=dict.get(dic,p)+1
        else:
            dic[p]=1
    return dic