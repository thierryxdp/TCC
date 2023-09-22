def inverte(frase):
    """Função que dada uma frase uma outra frase que contenha as mesmas palavras da frase de entrada de ordem inversa,
    str --> str"""
    f1 = str.replace(frase,'-',' ')
    f2 = str.replace(f1,':',' ')
    f3 = str.replace(f2,';',' ')
    f4 = str.replace(f3,'!',' ')
    f5 = str.replace(f4,'?',' ')
    f6 = str.replace(f5,',',' ')
    f7 = str.replace(f6,'.',' ')
    
    minuscula = str.lower(f7)
    lista_palavra = str.split(minuscula)
    lista_inversa = lista_palavra[::-1]
    return str.join(' ', lista_inversa)