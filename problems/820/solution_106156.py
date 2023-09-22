def posLetra(frase,letra,n):
    """retorna a posicao de uma certa letra em uma string apos um numero n de ocorrencais
    str, str, int -> int"""
    cont_ocorrencias, cont_pos = 0, 0
    while cont_pos < len(frase):
        if frase[cont_pos] == letra:
        	cont_ocorrencias += 1
        if cont_ocorrencias == n:
            return cont_pos
        cont_pos += 1
    return -1