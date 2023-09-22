def maiores(numero,n):
    """  Função  que dada uma lista de números inteiros e 
    um número n, retorna outra lista, com todos números 
    da lista maiores que n
    Entrada: list, int
    Saída: list """ 
    x = numero[:]
    y = [n]    
    list.sort(x)
    if n>x[0]:
        (soma) =x+y
        list.sort(soma)      
        return soma[n:]
    else:
        return x