def lingua_p(palavra):
    v = 'a,e,i,o,u'
    for x in palavra:
        if x in v:
            palavra = palavra.replace(x,x+'p'+x)
    return palavra