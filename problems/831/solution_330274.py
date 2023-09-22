def lingua_p(palavra):
    vogais = ["a","e","i","o","u","â","á","ã","é","ê","ó","ô"]
    codificado = ""
    for i in palavra.lower():
        if i in vogais:
            codificado += i+"p"+i
		else:
            codificado +=i
	return codificado