def freq_palavras(frases):
    '''A funcao recebe uma string e retorna a quantidade de vezes que uma palavra se
repetiu na forma de um dicionario str->dic'''
    div=frases.split(' ')
    dic={}
    for i in div:
        dic[i]=div.count(i)
    return dic