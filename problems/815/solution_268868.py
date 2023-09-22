def insere (lista_numero, n):
    """Funçao que recebe uma lista de numeros inteiros em ordem crescente, um numero n e inclui n na posicao onde a lista continua ordenada;
    entrada: list [[list], int];
    saida: list."""
    
    lista_numero = list.append (lista_numero [1], n)
    lista = list.sort (lista_numero)
    return lista