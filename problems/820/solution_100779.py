def posLetra(frase,letra,n):
    '''retorna a posicao da letra de acordocom a ocorrencia indicada;
    str,str,int->str'''
    a=-1
    x=0
    while x<n:
        a=str.find(frase,letra,a+1)
        x=x+1
    return a