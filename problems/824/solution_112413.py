def uppCons(string):
    '''Retorna a frase com todas as suas consoantes
       em maiúsculas e os demais inalterados; 
       str -> str'''
    contador = 0
    acumulador = ''
    while contador < len(string):
        if str.lower(string[contador]) not in 'aeiouáéíóúâêîôûãõ':
            acumulador = acumulador + str.upper(string[contador])
        else:
            acumulador = acumulador + string[contador]
        contador = contador + 1
    return acumulador