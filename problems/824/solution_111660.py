def uppCons(frase):
    """funcao que recebe como entrada uma frase e 
    retorna a mesma frase com as consoantes em 
    letra maiuscula.
    entrada- str
    saida- str
    """
    i=0
    nova=""
    while i<len(frase):
        if frase[i] not in "AÁÃÂEÉÊIÍÎOÓÔÕUÚaáãâeéêiíîoóôõuúû":
            nova=nova + str.upper(frase[i])
        if frase[i] in "AÁÃÂEÉÊIÍÎOÓÔÕUÚaáãâeéêiíîoóôõuúû":
            nova= nova +frase[i]
        i=i+1

    return nova