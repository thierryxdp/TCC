def lingua_p(palavra):
    """Recebe um string em portugues e a retorna traduzida para lingua do p; str->str."""
    for letra in palavra:
		if letra in "aeiou":
        	silaba_traduzida= letra+ "p" + letra
          	palavra_traduzida=silaba_traduzida +letra+ "p" + letra
    return palavra_traduzida