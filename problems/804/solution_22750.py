def filtra_pares(t):
    lista = [] # Aqui se declara uma lista, pois iremos modificá-la no loop, cosia que a tupla não nos permite.
    if type(t) == tuple and len(t) == 4:
        #Se o parâmetro enviado para função, for uma tupla de quatro itens, o procedimento será feito.
        for i in t:
            #Aqui faremos um loop para cada item na tupla.
            if type(i) != int:
                lista = []
                break
             elif i%2 == 0:
                 #Se ele for inteiro e par, será adicionado à lista.
                 lista.append(i)
        return(tuple(lista))