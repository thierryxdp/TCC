def maiores(a,b):
    'retorna uma lista com numeros maiores que o parametro escolhido'
    'entrada: list,int'
    'saida: list'
    x=a
    list.sort(x)
    list.partition(x,b)
    return x