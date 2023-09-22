def posLetra (string, letra, n):
    'dadas uma string, uma letra e um numero que indica uma posição, retoorna a posição da string em que a letra dada se repete pela "n" vez. str, str, int -> int'
    a = 0
    contador = 0
    while a < len(string)-1:
        if string[a] == letra:
            contador +=1
        if contador == n:
            return a
        a +=1
    return -1