def uppCons(texto):
    """Dado uma frase, retorna uma nova frase
com suas consoantes em letras maiúsculas. string-->string"""
    consoantes=[]
    i=0
    while i<len(texto):
        if str.lower(texto[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(consoantes,str.upper(texto[i]),)
        else:
            list.append(consoantes,texto[i],)
        i=i+1
    return str.join("",consoantes)