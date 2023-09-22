def inverte(frase):
    '''funccao que dada uma frase retorna a frase invertida.'''
    nova_frase = frase[:]
    for pnt in [".", ",", "-", "!", "?", ";", ":"]:
        nova_frase = str.replace(nova_frase, pnt, " ")
    lista = str.split(nova_frase)
    lista.reverse()
    nova_frase = str.join(" ", lista)
    return nova_frase.lower()