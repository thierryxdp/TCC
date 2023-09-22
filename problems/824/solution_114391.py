def uppCons(texto):
    """Dado um texto qualquer, retorna o texto com todas as consoantes em caixa alta:
    str-->str"""
    letras=len(texto)
    i=0
    while i<letras:
        if texto[i] not in 'aeiouAEIOUáéíóúÁÉÍÓÚãÃâêôÂÊÔ':
            texto=texto.replace(texto[i],texto[i].upper())
        i+=1
    return texto