def freq_palavras(palavra):  
    '''funçao que retorna o número de ocorrência de cada palavra da string de entrada''' 
    '''str->dict'''
    dic={}
    n=1
    lista=str.split(palavra) 
    for p in lista: 
        if p in dic: 
            dic[p]=dict.get(dic,p)+1
        else:
            dic[p]=1
    return dic