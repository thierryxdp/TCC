def uppCons(string):
    '''Retorna a frase com todas as suas consoantes
       em maiúsculas e os demais inalterados; 
       str -> str'''
    contador = 0
    acumulador = ''
    while contador < len(string):
        if string[contador] not in 'aeiouAEIOU':
            acumulador = acumulador + str.upper(string[contador])
        else:
            acumulador = acumulador + string[contador]
        contador = contador + 1
    return acumulador