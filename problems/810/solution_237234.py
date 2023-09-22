def inverte(texto):
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'.',' ')
    texto= str.replace(texto,'?',' ')
    texto= str.replace(texto,'!',' ')
    (texto.split())
    invertida = ' '.join(texto[-1::] for texto in texto.split())
    return invertida