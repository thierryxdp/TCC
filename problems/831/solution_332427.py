def lingua_p(palavra):
    '''funcao que recebe uma palavra e retorna uma palavra traduzida para lingua do p;
       str => str'''
    resultado = []
    contador = 0
    for i in list(palavra):
        if i in 'aeiouáéíóú':
            resultado = resultado+[i+'p'+i,]
        else:
            resultado = resultado + [i,]
    return ''.join(resultado)