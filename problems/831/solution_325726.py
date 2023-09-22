def lingua_p (palavra):
    '''Retorna a palavra inserida "palavra" traduzida para a "língua do P" que consiste em adicionar
    uma letra "p" para cada vogal na palavra e dobrando esta fazendo com que o "p" fique no meio de duas vogais;
    str -> str'''
    resultado = ""
    for l in range (len(palavra)):
        if palavra [l] in "qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM":
            resultado = resultado + palavra [l]
        else:
            resultado = resultado + palavra [l] + "p" + palavra [l]
    return resultado