def insere(lista_numero,n):
    """insero um numero e o coloca na posição correta
    list,float->list)"""
    x=lista_numero
    list.append(x,n)
    list.sort(x)
    return x
def maiores(lista,n):
    """função q recebe ma lista e um numero n e retorna uma lista com os numeros da lista maiores q n em ordem crescente
    list,int->list"""
    y=lista
    insere(y,n)
    return y[list.index(y,n)+1:]