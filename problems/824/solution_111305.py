def uppCons(frase):
    '''funcao que recebe uma frase e a retorna com as consoantes em maiúsculo;str-->str'''
    maiuscula=''
    posicao=0
    while posicao <len(frase):
        consoante= frase[posicao]
        if frase[posicao] in 'qwrtypsdfghjklçzxcvbnm':
        consoante=consoante.uppper()
        maiuscula= maiuscula + consoante
        posicao=posicao+1
    return maiuscula