def uppCons (frase):
    """
    	Função que retorna a frase dada com suas consoantes
        maiusculas.
    	string -> string
    """
    alfabeto = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    i = 0
    while i<len(frase):
        if frase[i] in alfabeto:
            frase = frase.upper(i)
        i = 0 + 1
    return frase