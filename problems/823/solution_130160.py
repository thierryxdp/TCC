def faltante(lista):

    n=len(lista)+1

    i=0

    nlista=[None]*n

    while i<n:

        nlista[i]=0

        i+=1

    i=0

    while i<n-1:

        nlista[lista[i]-1]=1

        i+=1

    i=0

    while i<n:

        if(nlista[i]==0):

            return i+1

        i+=1