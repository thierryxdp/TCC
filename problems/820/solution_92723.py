def posLetra(string,l,n):
    '''retorna a posição da string onde a occorência n da letra acontece
    str,str,int->int'''
    indexacao=''
    i=0
    while i<len(string):
        if l in string:
            o1=str.find(string,l)
        i=i+1
        indexacao=indexacao+o1
    return sum.indexacao