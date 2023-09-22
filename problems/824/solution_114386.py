def uppCons(frase):
    """Função que recebe uma frase e retorna essa mesma frase porém com
    todas as consoantes em maiúsculo"""
    volta=""
    indice=0
    while indice<len(frase):
        if frase[indice] in 'qwrtypsdfghjklzxcvbnmç':
            volta=volta+(str.upper(frase[indice]))
        else:
            volta=volta+frase[indice]
        indice=indice+1
    return volta