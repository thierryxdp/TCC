def uppCons(frase):
    """Função que recebe uma frase, e retorna a frase com todas consoantes maiúsculas"""
    indice=0
    while indice<len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            str.replace(frase,frase[indice],str.upper(frase[indice])
        indice+= 1
    return frase