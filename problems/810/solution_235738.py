def inverte (frase):
    """Função que tem como entrada uma frase e retorna outra frase sem letras maiúsculas, pontução e invertida
    string -> string"""
    x = frase
    a = str.replace (x,'.',' ')
    b = str.replace (a,',',' ')
    c = str.replace (b,'-',' ')
    d = str.replace (c,';',' ')
    e = str.replace (d,':',' ')
    f = str.replace (e,'?',' ')
    g = str.replace (f,'!',' ')
	h = str.split (g,' ')
    i = str.lower (h)
    j = i[::-1]
    l = str.join (' ',j)
    return l