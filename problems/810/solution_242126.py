def inverte(frase):
    """
    	Retorna a frase dada sem pontuação, sem maiúscula e invertida
    	str -> str
    """
    frase_split=str.split(str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),'?',' '),'.',' '),'-',' '),',',' '),':',' '),';',' ')))
    list.reverse(frase_split)
    return str.join(' ', frase_split)