def filtra_pares(x):
    '''Essa função dado os parâmetros, filtra os
os elementos pares e retorna uma tupla contendo os elementos filtrados
int,int,int,int->tuple'''
lista=[]
if type(x)==tuple and len(x)==4:
    for n in x:
     if n%2==0:
        lista.append(n)
       return tuple(lista)