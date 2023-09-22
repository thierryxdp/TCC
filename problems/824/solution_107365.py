def uppCons(frase):
    """Retorna uma frase com todas as consoantes em maiusculas.str-->str"""
	s=frase
    i=0
    frase_nova=""
    while i<=len(s):
        if s[i] not in "AEIOUaeiou":
            frase_nova=frase_nova+s[i].upper()
        if s[i] un "AEIOUaeiou":
            frase_nova=frase_nova+s[i]
        i=i+1
    return frase_nova