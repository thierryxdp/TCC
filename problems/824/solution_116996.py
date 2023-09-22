def uppCons(frase):
    """dada uma string frase de entrada, retorna a mesma string no entanto com
    os caracteres consoantes em maiusculo
    str --> str"""
    contador=0
    lista_frase=str.split(frase, '')
    while contador < len(lista_frase):
        if lista_frase[contador] in 'bcdfghjklmnpqrstvxywzç':
            lista_frase[contador]=lista_frase.upper()
        contador=contador+1
    return lista_frase