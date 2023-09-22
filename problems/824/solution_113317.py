def uppCons(frase):

    frasefinal =""

    k = 0

    while k<len(frase):

        if frase[k] not in "aeiouáéíóúàèìòùâêîûôãõ":

            frasefinal = frasefinal + str.upper(frase[k])

        else:

            frasefinal = frasefinal + frase[k] 

        k = k + 1

    return frasefinal