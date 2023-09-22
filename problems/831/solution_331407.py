def lingua_p(palavra):
    palavra.lower
    palavranova=""
    for i in range(len(palavra)):
        if palavra[i] in "aeiouáéíóúêôãõ":
            palavranova = palavranova+palavra[i]+"p"+palavra[i]
        else:
            palavranova=palavranova+palavra[i]
    return palavranova