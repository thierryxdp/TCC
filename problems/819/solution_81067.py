def filtraMultiplos(lista,n):
    "Função que dado uma lista númera, retorna uma lista com os multiplos de n dado de entrada. list, int --> list"
    mults=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            mults=mults+[lista[i]]
        i=i+1
    return mults