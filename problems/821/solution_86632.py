def fatorial (numero):
    """Função que dado um número, calcula a fatorial deste numero;
        int -> int."""
    lista= list (range(numero, 0, -1))
    i= 0
    j= 1
    while i < len (lista):
        j= j*lista[i]
        i+=1 
    return j