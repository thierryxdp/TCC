def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiusculo
    str -> str'''
    i=0
    consoante = str(b,'c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    consoante = consoante.upper()
    while consoante in frase:
        i += 1
        return frase