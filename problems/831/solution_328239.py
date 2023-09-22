def lingua_p(palavra):
    '''Funcao que retorna a palavra de entrada traduzida na lingua do P.
    str->str'''
    p=[]
    for l in palavra:
        if letra in 'aeiouàáâãéêíóôõú':
            x=l+'p'+l
            list.append(p,x)
        else:
            list.append(p,letra)
    return str.join('',p)