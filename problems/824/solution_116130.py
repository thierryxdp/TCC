def uppCons(texto):
    '''Funcao recebe um texto e retorna suas consoantes em letra miusculas. Todas as outras letras ficam com sua formatacao inserida
string -> string'''
    contador = 0
    string = ''
    while(contador<len(texto)):
        if texto[contador] in 'bcdfgçhjklmnpqrstvxywz'):
            string += str.upper(texto[contador])
        else:
            string += texto[contador]
        contador += 1
    return string