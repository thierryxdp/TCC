def altera_frase(frase,palavra,posicao):
    '''
    Dado uma frase, uma palavra e uma
    posição altera a frase.
    '''
    f = frase
    pal = palavra
    pos = posicao
    fs = f.split()
    if pal in fs:
        list.insert(fs,list.index(fs,pal),pal.upper())
        return (' '.join(fs[0:list.index(fs,pal)] + fs[list.index(fs,pal)+1:]))
    else:
        f3=f.split()
        list.insert(f3,pos,pal)
        return (' '.join(f3))