def posLetra(string,letra,num):
    soma=0
    i=1
    x=str.count(string,letra)
    if x!=num:
        return -1
    while i<len(string):
        soma=soma+1
    i=i+1
    return soma