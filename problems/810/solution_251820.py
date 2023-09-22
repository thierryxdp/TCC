def inverte(frase):
    """funcao que retorna a frase so que de maneira inversa;
    str->str"""
    minusc=str.lower(frase)
    rempont= rempontuacao(minusc)
    lista_frase=str.split(rempont)
    lista_invertida=lista_frase[::-1]
    return lista_invertida