def uppCons(texto):
    ''' Função recebe frase e retorna com todas as sua consoantes
    em maiúsculas. '''
    lista = list(texto)
    i = 0
    letras = []
    while i < len(lista):
        if lista[i] in 'çbcdfghjklmnpqrstvwxyz':
            letras.insert(i,lista[i].upper())
            i += 1
        else:
            letras.insert(i,lista[i])
            i += 1
            
    return ''.join(letras)