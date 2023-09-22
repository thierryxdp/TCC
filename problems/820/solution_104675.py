def posLetra(s,l,n):
    '''funçao que retorna em qual posição da string determinada
    letra está; str,str,int->int'''
    i=0
    p=''
    while i<=len(s):
        if l in s:
            if n>str.count(s,l):
                return -1
            else:
                return str.find(s,l,n-1)
            i=i+1