def lista(a,b):
    'adiciona e ordena os elementos da lista'
    'entrada: list,int'
    'saida: list'
    x=a
    list.append(x,b)
    list.sort(x)
    return x
def maiores(a,b):
    'retorna uma lista com numeros maiores que o parametro escolhido'
    'entrada: list,int'
    'saida: list'
    z=lista(a,b)
    x=list.index(z,b)
    k=z[x+1:]
    return k