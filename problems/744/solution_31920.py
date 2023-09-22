def hashtag(s):
    """Função que recebe uma string e insere o caractere '#'
    no início, no meio e no final dela.
    str->str"""
    l=len(s)
    d=int(l/2)
    return "#"+s[0:d]+"#"+s[d:]+"#"