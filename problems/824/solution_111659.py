def uppCons(frase):
    """ """
    i=0
    nova=""
    while i<len(frase):
        if frase[i] not in "AÁÃÂEÉÊIÍÎOÓÔÕUÚaáãâeéêiíîoóôõuúû":
            nova=nova + str.upper(frase[i])
        if frase[i] in "AÁÃÂEÉÊIÍÎOÓÔÕUÚaáãâeéêiíîoóôõuúû":
            nova= nova +frase[i]
        i=i+1

    return nova