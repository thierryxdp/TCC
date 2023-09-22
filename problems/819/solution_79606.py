def filtraMultiplos(num,n):
    """com base na lista de numeros num, verifica quais elementos sao divisiveis
    por n
    list,int -> list"""
    lista=[]
    i=0
    while i<len(num):
        if num[i]%n==0:
            lista.append(num[i])
        i=i+1
    return lista