def lingua_p(palavra: str) -> str:
    palavra = palavra.lower()
    palavraP = ""
    for i in palavra:
        if i in "aeiou":
            palavraP += i + "p" + i
        else:
            palavraP += i
	return palavraP