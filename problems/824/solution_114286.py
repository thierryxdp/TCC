def uppCons(frase):
    '''função que dada uma frase retorna a msm frase com as consoantes em maiuscúlas
    e o restante da msm forma que estavam originalmente'''
    proximo=  0
    newfrase=''
    while proximo < len(frase):
        if frase[proximo] in "qwrtypsdfghjklçzxcvbnm":
            if frase[:proximo] not in newfrase:
            	newfrase= newfrase + frase[:proximo]
        newfrase= newfrase + str.upper(frase[proximo])
        proximo= proximo + 1
    return frase