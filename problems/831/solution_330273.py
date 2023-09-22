def lingua_p(palavra):
    vogais = ["a","e","i","o","u"]
    codificado = ""
    for i in palavra.lower():
        if i in vogais:
            codificado += i+"p"+i
		else:
            codificado +=i
	return codificado