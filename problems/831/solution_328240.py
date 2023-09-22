def lingua_p(palavra):
    '''Funcao que retorna a palavra de entrada traduzida na lingua do P.
    str->str'''
    p=[]
    for l in palavra:
        if l in 'aeiouàáâãéêíóôõú':
            x=l+'p'+l
            list.append(p,x)
        else:
            list.append(p,l)
    return str.join('',p)