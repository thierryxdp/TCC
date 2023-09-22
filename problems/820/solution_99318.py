def posLetra(frase,l):

    r=()

    i=0

    whie i < len(frase):

        if l in frase[i]:

            r= r+(i)

        i=i+1

    return r