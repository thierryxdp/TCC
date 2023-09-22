def inverte(p):
    def retira_pontuacao(p):
    if "." in p:
        p = str.replace (p, ".", " ", str.count(p, "."))
	if "," in p:
        p = str.replace (p, ",", " ", str.count(p, ","))
	if ":" in p:
        p = str.replace (p, ":", " ", str.count(p, ":"))
	if ";" in p:
        p = str.replace (p, ";", " ", str.count(p, ";"))
	if "-" in p:
        p = str.replace (p, "-", " ", str.count(p, "-"))
	if "!" in p:
        p = str.replace (p, "!", " ", str.count(p, "!"))
	if "?" in p:
        p = str.replace (p, "?", " ", str.count(p, "?"))
	p = (str.split(str.lower(p)))
    list.reverse (p)
    z = " "
    return z.join(y)