def uppCons(frase):
        
        lista = [i for i in frase]

        lista = list(map(str.upper, lista))

        saida = ''

        for i in lista:

                saida += i

        return saida