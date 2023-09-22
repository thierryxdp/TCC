def lingua_p(palavra):
    """Funcao recebe uma palavra e a retorna na lingua P
    str -> str"""
    palavra = palavra.lower()
    palavra = list(palavra)
    lugar = []
    j = 0
    for i in range(len(palavra)):
        if palavra[i] in "aeiouãéáúóâô":
            lugar.insert(j,palavra[i])
            lugar.insert(j+1,"p")
            lugar.insert(j+2,palavra[i])
            j = j + 3
        else:
            lugar.insert(j,palavra[i])
            j = j + 1
    p = "".join(lugar)
    return p