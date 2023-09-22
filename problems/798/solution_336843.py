def freq_palavras(text):
    '''Dado uma frase, a função retornará 
um dicionario onde nele estará contido as 
palavras junto da quantidade de vezes que 
se repetem.
       str->dict'''
    x=text.split(' ')
    dic={}
    for i in range(len(x)):
        substring=x[i]
        text.count(substring)
        dic[x[i]]=x.count(substring)
    return dic