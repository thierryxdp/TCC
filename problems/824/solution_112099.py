def maiusculo(char):

        if not char in "aeiouáàéèíìóúâêã":

                return char.upper()

        return char



def uppCons(frase):
        
        lista = [i for i in frase]

        lista = list(map(maiusculo, lista))

        saida = ''

        for i in lista:

                saida += i

        return saida