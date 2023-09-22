def inverte(frase):
    """funçao que retira pontuaçao e maiusculas e inverte a ordem da frase
    str -> str)"""
    texto=str.replace(frase,',',' ')
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,'.',' ')
    texto=str.replace(texto,'!',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,';',' ')
    texto=str.replace(texto,':',' ')
    texto=str.lower(texto)
    lista=str.split(texto,' ')
    inverter=lista[::-1]
    frase_invertida=str.join(' ',inverter)
    return frase_invertida