def lingua_p(palavra):
    """Reecebe um string em portugues e a retorna traduzida para lingua do p; str->str."""
    for letra in palavra:
		if letra in "aeiou":
            palavra_traduzida= letra+ "p" + letra
    return palavra_traduzida