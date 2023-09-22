def inverso(frase):
	if ":" in frase:
		frase = frase.replace(":", "")
	if ";" in frase:
		frase = frase.replace(";", "")
	if "." in frase:
		frase = frase.replace(".", "")
	if "!" in frase:
		frase = frase.replace("!", "")
	if "-" in frase:
		frase = frase.replace("-", "")
	if "," in frase:
		frase = frase.replace(",", "")
	if "?" in frase:
		frase = frase.replace("?", "")
	f1 = frase.split(" ")
	f2 = len(f1)+1
	f3 = f1[-1:-(f2):-1]
	inverso = str.join(’ ’,f3)
	return str.lower(inverso)