def uppCons(frase):
    contador = 0
    consoantes = ("qwrtypsdfghjklçzxcvbnm")
    d = str.upper(frase)
    while contador < len(frase):
        if frase[contador] in consoantes:
           frase =str.replace(frase,frase[contador],str.upper(frase[contador]))
        contador = contador + 1

    return frase