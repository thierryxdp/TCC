def posLetra(string, letra, num):
    """Retorna a posição de uma string onde uma letra de entrada está; string, string, int -> int."""
    i = 0
    x=[]
    while i < len(string):
        if string[i] == num:
            list.append(x, i)
        else:
            i = i + 1
    if len(x) == num:
            return x[(len(x)-1)]