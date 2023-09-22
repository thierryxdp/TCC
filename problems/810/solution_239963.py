def inverte(texto):
    """função que retorna a frase de entrada com a ordem invertida
    Entrada: str
    Saída: str"""
    texto=str.replace(texto,',',' ')
    texto=str.replace(texto,'.',' ')
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,':',' ')
    texto=str.replace(texto,';',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,'!',' ')
    texto=str.replace(texto,'...',' ')
    x=str.split(texto)
    z=x[::-1]
    y=str.join(' ',z)
    return str.lower(y)