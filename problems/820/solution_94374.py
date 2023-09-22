def posLetra (f,l,n):
    """Função que recebe como entrada uma frase e uma palavra em string
    e um número n, devendo retornar em que posição da string há a ocorrência
    (n) da letra, caso não haja menos ocorrências do que o pedido, deve retornar
    -1.
    str,str,int-> int
    """
    n_ocorrencias= str.count (f,l)

    if n_ocorrencias < n:
        return -1
    else:
        f= str.replace (f, l, ' ', n-1)
        return str.find (f,l)