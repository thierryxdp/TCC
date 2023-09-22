def faltante (lista):
    """funçao que recebe uma lista  de 1 - n ou n -1 onde n sao numeros inteiros e positivos e retorna o numero faltante na sequencia
entrada: list;
saida : int."""

    list.sort (lista)
    fim = lista [-1]
    ideal = list (range (1, fim +1))
    pos = 0

    while pos < len (lista):
        if ideal [pos] in lista:
            pos = pos + 1
        
        else:
            return ideal [pos]