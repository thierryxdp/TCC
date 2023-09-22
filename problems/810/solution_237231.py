def inverte(texto):
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'.',' ')
    texto= str.replace(texto,'?',' ')
    texto= str.replace(texto,'!',' ')
    string = texto[::-1]
    return string