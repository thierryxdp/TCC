def filtraMultiplos(lista,n):
    """dada uma lista e um número n, a função retorna uma nova lista
    apenas com os elementos múltiplos n.
    list,int-->list
    
    Parâmetros
    lista: lista de números utilizada como entrada
    n: núemro utilizado como entrada. A lista final será composta
    por múltiplos de n"""
    novalista=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            list.append(novalista,lista[i])
        i=i+1
    return novalista