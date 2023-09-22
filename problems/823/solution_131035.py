def faltante (lista):
    """funçao que recebe uma lista com uma sequencia de numeros com um faltante e retorna o numero que falta na sequencia;
entrada: list
saida: int."""
    x = len (lista)+ 1
    lista.sort ()
    i = 0
    while i < x:
        if i + 1 not in lista:
            return i+1
        if lista [i] != i+1:
            return i+1
        else:
            i += 1