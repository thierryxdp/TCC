def lingua_p(palavra):
	inicio = 0
    for letra in list(palavra):
        if letra in 'aeiou':
            palavra = palavra[0:str.index(palavra,letra,inicio)] + letra + "p" + letra + palavra[str.index(palavra,letra,inicio)+1:]
            inicio = str.index(palavra,letra,inicio) + 3
    return palavra