def uppCons(frase):
    '''dada uma frase, retorna outra frase com as consoantes da frase original em letra maiuscula; str -> str'''
    i = 0
    lista = []
    lista[:] = frase
    nova_lista = []
    while i<len(lista):
        if lista[i] in 'bcdfghjklmnpqrstvwxyzç':
            lista[i].upper()
            nova_lista = nova_lista + [lista[i]]
        else:
            nova_lista = nova_lista + [lista[i]]
        i = i + 1
    return ''.join(nova_lista)