def uppCons(frase):
    '''função que retorna todas as maiusculas em CAPSLOCK
    str -> str'''
    lc = len(frase)
    i = 0
    nf = []
    while i < lc:
        if frase[i] != ("a")  and frase[i] != ("ã") and frase[i] != ("e") and frase[i] != ("é") and frase[i] != ("i") and frase[i] != ("í") and frase[i] != ("o")  and frase[i] != ("ó") and frase[i] != ("u") and frase[i] != ("ú"):            
            list.append(nf,(str.upper(frase[i])))
        else:
            list.append(nf,frase[i])
        i = i + 1
    
    return ''.join(nf)