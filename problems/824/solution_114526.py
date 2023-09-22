def uppCons(txt):
    """Função que retorna a frase com todas as suas consoantes em maiúsculas"""
    """str->str"""
    consoantes=('bcdfghjklmnpqrstvwxyz')
    x=0
    novotxt=""
    while x<len(txt):
        if txt[x] in consoantes:
            txtnovo+= str.upper(txt[x])
        else:
            txtnovo += txt[x]
        x+=1
    return txtnovo