def posLetra(string,letra,n):
    ''' funcao retorna a posicao da letra na string. str,str,int->int'''
    i=0
    a=0
    while i+1<=len(string):
        if string[i]==letra:
            a+=1
            if a==n:
                break
        i+=1
    if a==n:
        return i
    else:
        return -1