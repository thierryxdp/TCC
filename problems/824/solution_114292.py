def uppCons(frase):
    '''função que dada uma frase retorna a msm frase com as consoantes em maiuscúlas
    e o restante da msm forma que estavam originalmente'''
    proximo=  0
   
    while proximo < len(frase):
        if frase[proximo] in "qwrtypsdfghjklçzxcvbnm":
            uppalavra= str.upper(frase[proximo])
            str.replace(frase,frase[proximo],uppalavra)
        proximo= proximo + 1
    return frase