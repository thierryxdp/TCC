from math import *
def lingua_p(palavra):
    '''
    Dado uma palavra em português, retorna a mesma palavra para língua do P.

    Uso:
    lingua_p(palavra)

    Entrada:
    - palavra (str): Palavra a ser "traduzida" para a língua do p

     Saída:
    - Retorna a palvra na língua p. (str)
    '''
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP