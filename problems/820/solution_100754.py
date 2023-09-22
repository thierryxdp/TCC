def posLetra(frase,letra,n):
    '''retorna a ultima posicao em que a letra selecionada se encontra;
    str,str,int->str'''
    if str.count(frase,letra)<n:
        return -1
    a=0
    x=0
    while a<str.count(frase,letra):
        a=str.find(frase,letra,x)
        x=x+1
    return a