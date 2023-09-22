def conta_frases(texto):
    """Conta o número de frases que aparecem no texto, que é o parâmetro
       str --> int"""
	int a = texto.count(texto,".")
	int b = texto.count(texto,"...")
	int c = texto.count(texto,"?")
	int d = texto.count(texto,"!")
	return texto = a + b + c + d