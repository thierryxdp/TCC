def inverte(frase):
    frase=retira_pontuacao(frase)
    if '.':
    	frase = str.split(frase, ".")
    	frase = str.join(" ", frase)
    if ',':
        frase = str.split(frase, ",")
    	frase = str.join(" ", frase)
    if '...':
        frase = str.split(frase, "...")
    	frase = str.join(" ", frase)
    if '?':
        frase = str.split(frase, "?")
    	frase = str.join(" ", frase)
    if '-':
        frase = str.split(frase, "-")
    	frase = str.join(" ", frase)
    if ':':
        frase = str.split(frase, ":")
    	frase = str.join(" ", frase)
    if '!':
        frase = str.split(frase, "!")
    	frase = str.join(" ", frase)
    str.lower(frase)
    aux=frase.split()
    aux[: :-1]
    frase=str.join(" ',aux)
    return frase