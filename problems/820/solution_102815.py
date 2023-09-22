def posLetra(string, letra, numero):
    """dada uma string, uma letra e um numero inteiro de entrada
    retorna em qual indice está a ocorrencia numero desejada
    caso exista menos ocorrencias do que o numero desejado a função retorna -1
    str, str, int --> int"""
    contador=0
    contador2=0
    ocorrencias=string.count(letra)
    if numero > ocorrencias:
        return -1
    else:    
        while contador2 < numero:
            if string[contador]==letra:
                contador2=contador2+1
            contador=contador+1
    return contador-1