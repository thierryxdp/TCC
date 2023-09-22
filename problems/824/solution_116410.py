def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiusculo
    str -> str'''
    frase = [i]
    i=1
    consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    while consoante in frase:
        consoante = frase[i]
        novafrase = frase[i].capitalize
        i += 1
        return novafrase