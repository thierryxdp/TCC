def filtra_pares(tupla):
    "função que recebe uma tupla com quatro elementos a,b,c,d e retorna uma nova tupla com os elementos pares da tupla anterior"
  	tupla1=[]
    for x in tupla:
        if x%2==0:
            tupla1.append(x)
    tupla1=tuple(tupla1[:])
    return tupla1