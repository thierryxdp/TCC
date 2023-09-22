def posLetra(stri,letr,num):
    """
    	retorna a posição de uma determinada ocorrência de uma string, na string dada
    	str,str,int -> int
    """
    qnt_letr=0
    i=0
    while qnt_letr<stri.count(letr):
        if num > stri.count(letr):
            return -1
        elif stri[i]==letr:
            qnt_letr += 1
        elif qnt_letr == num:
            return i
        i+=1