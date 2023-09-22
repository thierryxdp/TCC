def posLetra(string,letra,n):
    '''dada uma string, uma letra pertencente a ela e um numero n, retorna a posicao na string em que ha a n-esima ocorrencia da letra dada como parametro; str,str,int -> int'''
   
    i = 0
    cont = 0
    while i<len(string):
        if string[i] == letra:
            cont = cont + 1
        i = i + 1
        if cont == n:
            return i
    return -1