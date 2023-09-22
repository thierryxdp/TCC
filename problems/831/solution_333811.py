def lingua_p(palavra):
    lista = []
    i = 0
    for elemento in list(palavra):
        if elemento in 'aeiouáéíóúàèìòùãõ':
            lista.append(elemento + "p" + elemento)
        else:
            lista.append(elemento)
    return ''.join(lista)