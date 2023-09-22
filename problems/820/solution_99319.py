def posLetra(frase,l):

    r=()

    i=0

    while i < len(frase):

        if l in frase[i]:

            r= r+(i)

        i=i+1

    return r