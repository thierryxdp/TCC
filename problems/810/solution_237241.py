def inverte(texto):
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'.',' ')
    texto= str.replace(texto,'?',' ')
    texto= str.replace(texto,'!',' ')
    texto_separado = texto.split()
    texto_invertido = (texto_separado[::-1])
    separador = " "
    texto_finalizado = separador.join(texto_invertido)
    return(str.lower(texto_finalizado))