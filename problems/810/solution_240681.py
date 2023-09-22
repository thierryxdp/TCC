def inverte(frase):
    if '.':
    	frase = str.split(frase, ".")
    	frase = str.join(" ", frase)
        str.lower(frase)
    if ',':
        frase = str.split(frase, ",")
    	frase = str.join(" ", frase)
        str.lower(frase)

    if '...':
        frase = str.split(frase, "...")
    	frase = str.join(" ", frase)
        str.lower(frase)

    if '?':
        frase = str.split(frase, "?")
    	frase = str.join(" ", frase)
        str.lower(frase)

    if '-':
        frase = str.split(frase, "-")
    	frase = str.join(" ", frase)
        str.lower(frase)

    if ':':
        frase = str.split(frase, ":")
    	frase = str.join(" ", frase)
        str.lower(frase)

    if '!':
        frase = str.split(frase, "!")
    	frase = str.join(" ", frase)
        str.lower(frase)

    return str.lower(frase)[-200:]