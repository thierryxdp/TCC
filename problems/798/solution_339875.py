def freq_palavras(string):
    '''Função que transformar uma string em um dicionario;
    Recebe uma palavra;
    Retorna um dicionario.'''
    x = str.split(string)
    dic = {}
    for i in x:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic