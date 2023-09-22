def insere (lista_numero, n):
    """Funçao que recebe uma lista de numeros inteiros em ordem crescente, um numero n e inclui n na posicao onde a lista continua ordenada;
    entrada: list, int;
    saida: list."""
    
    list.append (lista_numero, n)
    list.sort (lista_numero)
    
    return lista_numero