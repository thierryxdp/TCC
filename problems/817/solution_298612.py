import math
def lista(a,b):
    'adiciona e ordena os elementos da lista'
    'entrada: list,int'
    'saida: list'
    x=a
    list.append(x,b)
    list.sort(x)
    return x
def maiores(a):
    'retorna uma lista com numeros maiores que a media'
    'entrada: list,int'
    'saida: list'
    b=math.floor(sum(a)/len(a))
    z=lista(a,b) 
    x=list.index(z,b)
    k=z[x+1:]
    return k