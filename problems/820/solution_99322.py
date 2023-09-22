def posLetra(frase,l,n):

    r=()

    i=0

    while i < len(frase):

        if l==frase[i]:

            r= r+(i)

        i=i+1

    return r