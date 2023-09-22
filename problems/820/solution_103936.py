def posLetra(frase, letra, pos):
    x=len(frase)
    nova_frase=str.index(frase,letra)
    nova_frase2=str.count(frase,letra)
    i=0
    a=0
    if 1==pos:
        return nova_frase
    elif nova_frase2<pos:
        return -1