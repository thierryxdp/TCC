def lingua_p(palavra):
    '''retorna a palavra na língua do p'''
    trad=''
    for i in palavra:
        if i in 'AEIOUaeiouáéíóúãõ':
            i=i+'p'+i
    return str.lower(trad)