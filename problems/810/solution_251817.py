def inverte(frase):
    """funcao que retorna a frase so que de maneira inversa;
    str->str"""
    minusculo=str.lower(frase)
    rempont=rempontuacao(minusculo)
    lista_frase=str.split(rempont)
    lista_invertida=lista_frase[::-1]
    return lista_invertida