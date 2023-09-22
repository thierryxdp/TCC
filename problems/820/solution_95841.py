def posLetra(frase,letra,n):
    #Dado uma frase, uma letra e um número que indica a ocorrência, retorna a sua posição na frase. str, str, int -> int.
    contador = 0
    i = 0
    while i in range(len(frase)):
        if frase[i] == letra:
            contador += 1
            if contador == n:
                return i
        i += 1
    return -1