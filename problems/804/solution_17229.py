def filtra_pares(t):
    lista = [] # Aqui se declara uma lista, pois iremos modificá-la no loop, cosia que a tupla não nos permite.
    if type(t) == tuple and len(t) == 4:
        #Se o parâmetro enviado para função, for uma tupla de quatro itens, o procedimento será feito.
         #Senão, um aviso será exibido.
        for i in t:
            #Aqui faremos um loop para cada item na tupla, caso ele não for inteiro um aviso será dado, e aquela lista inicial será limpa, para que quando o loop for parado pelo break, o resultado estar vazio.
            if type(i) != int:
                lista = []
                return('Todos os itens da tuplas devem ser inteiros.')
                break
            elif i%2 == 0:
                 #Se ele for inteiro e par, será adicionado à lista.
                 lista.append(i)
        return(tuple(lista)) #A lista é transformada em tupla e o resultado é exibido quando o loop acabar.
    else:
        return('Apenas será aceito, uma tupla, com quatro itens.')