def retira_pontuacao(p):
    if "." in p:
        p = str.replace (p, ".", " ")
	if "," in p:
        p = str.replace (p, ",", " ")
	if ":" in p:
        p = str.replace (p, ":", " ")
	if ";" in p:
        p = str.replace (p, ";", " ")
	if "-" in p:
        p = str.replace (p, "-", " ")
	if "!" in p:
        p = str.replace (p, "!", " ")
	if "?" in p:
        p = str.replace (p, "?", " ")
    return p