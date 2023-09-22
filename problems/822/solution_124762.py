def repetidos(lista):

        saida = 0
        
        tamanho = len(lista)

        lista2 = [lista[i] for i in range(1, tamanho)]

        lista2 = zip(lista, lista2)

        for i in lista2:

                if i[0] == i[1]:

                        saida += 1

        return saida