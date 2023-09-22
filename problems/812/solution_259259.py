def retirar(char):

        if char in "-:;.,!?":

                return " "
        
        return char



def retira_pontuacao(frase):

        saida = ""

        lista = [i for i in frase]

        lista = list(map(retirar, lista))

        for i in lista:

                saida += i

        return saida