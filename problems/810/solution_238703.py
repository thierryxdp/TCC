def invert(x):
    """Funçao que inverte os dados do parametro dado
    string -> string"""
    x1 = str.replace(x,'-',' ')
    x2 = str.replace(x1,':',' ')
    x3 = str.replace(x2,';',' ')
    x4 = str.replace(x3,'!',' ')
    x5 = str.replace(x4,'?',' ')
    x6 = str.replace(x5,',',' ')
    x7 = str.replace(x6,'.',' ')
    minuscula = str.lower(x7)
    lista_palavra = str.split(minuscula)
    lista_inversa = lista_palavra[::-1]
    return str.join(' ', lista_inversa)