def uppCons(frase):
    '''função que dada uma frase retorna a msm frase com as consoantes em maiuscúlas
    e o restante da msm forma que estavam originalmente'''
    proximo=  0
    
    while proximo < len(frase):
        if frase[proximo] in "qwrtypsdfghjklçzxcvbnm":
            frase[proximo]= str.upper(frase[proximo])
        proximo= proximo + 1
    return frase