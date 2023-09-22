def posletra(string,ltr,num):
    '''retorna a ocorrencia desejada da letra entre as palavras na str
    str,str,int --> int'''
    for i,n in enumerate(string):
        if ltr == n and num == 1: return i
        if ltr == n: num -= 1
    return -1