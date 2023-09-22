def inverte (frase):
    """ função que receba uma frase calcula e retorne uma frase"""
    """str->str"""
    um= str.replace (frase,'-',' ')
    dois = str.replace (um,',',' ')
    tres = str.replace (dois,':',' ')
    quatro = str.replace(tres,';',' ')
    quinto = str.replace(quatro,'.',' ')
    sexto = str.replace (quinto,'!',' ')
    setimo = str.replace (sexto,'?',' ')
    semponto = setimo
    
    minusculas = str.lower (semponto)
    
    split = str.split (minusculas)