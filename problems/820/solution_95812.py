def posLetra(frase, letra, vezes):
    #Essa função irá receber uma frase em string, e depois uma letra pela variável letra
    # e um número que vai indicar a ocorrência desejada e irá devolver a posição do string
    #que a letra está.
    #Entrada: String, string, int | Saída: Int

    i = 0
    aux = 0

    while i < len(frase):
        if frase[i] == letra:
            aux += 1

        if aux == vezes:
            return i
        i += 1

    return -1