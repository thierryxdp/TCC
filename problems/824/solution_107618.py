def uppCons(frase):
	'''Dada uma frase, retorna a frase com todas as consoantes em letras
    maiúsculas string -> string'''
    i = 0
    fraseFinal = list(frase)
    while (i < len(frase)):
        if (fraseFinal[i] not in 'AEIOUaeiouÁÉÍÓÚáéíóú'):
            list.insert(fraseFinal,i,fraseFinal[i].upper())
            del fraseFinal[i+1]
        i = i + 1
    return str.join('',fraseFinal)