def filtra_pares(x):
    '''Essa função dado os parâmetros, filtra os
os elementos pares e retorna uma tupla contendo os elementos filtrados
int,int,int,int->tuple'''
type(x)==tuple and len(x)==4
a=x[0]%2
b=x[1]%2
c=x[2]%2
d=x[3]%2
lista=[a,b,c,d]
if a==0 and b==0 and c==0 and d==0:
    return (lista)