def uppCons(frase):
    """Função que ao receber uma frase, retorna a frase com todas as
    consoantes maiúsculas, e os demais caracteres ficam idênticos em
    relação a frase original;
    str -> str"""
    frasef = ""
    i = 0
    while (i < len(frase)):
        if frase[i] not in "AEIOUaeiouãáéíóúõ":
            frasef = frasef+(str.upper(frase[i]))
        elif frase[i] in "AEIOUaeiouãáéíóúõ":
            frasef =  frasef+(frase[i])
        i += 1
	return frasef