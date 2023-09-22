def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a frase com todas as suas
consoantes em maiúsculas e os demais caracteres exatamente como estavam na
frase original.'''
    i = 0
    c = ['b','c', 'ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','w','y','z']
    frase2 = ''
    while i < len(frase):
        if frase[i] in c:
            frase2 += frase[i].upper()
        else:
            frase2 += frase[i]
        i = i+1

    return frase2