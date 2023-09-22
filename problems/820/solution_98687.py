def posLetra(string, letra, ocorrencias):
    '''Retorna a posição da string em que a ocorrência pedida
       da letra está;
       str, str, int -> int'''
    if string.count(letra) < ocorrencias:
        return -1
    else:
        contador = 0
        acumulador = string
        while contador < ocorrencias - 1:
            acumulador = acumulador[acumulador.index(letra)+1:]
            contador =  contador + 1
        return acumulador.index(letra) + len(string) - len(acumulador)