def conta_frases(frase):
    """Dada diversas frases, a função irá filtrar a quantidade de frases e retornar o valor.
	Cada frase precisa terminar com um ponto final, reticências, exclamação ou interrogação.
    Aceita valores do tipo string e retorna um valor do tipo inteiro, que será a quantidade de frases que a função possui."""
    x = frase.count(".")
    y = frase.count("...")
    a = frase.count("?")
    b = frase.count("!")
    x = x-3*y
    return x + y + a + b