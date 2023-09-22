def filtraMultiplos(listaNum, num):
    '''Essa funcao recebe como argumento lista de numeros e um numero.
       eh verificado se, cada elemento da lista eh divisivel pelo
       numero do segundo argumento. Caso seja divisivel, o numero eh
       armazenado em uma lista e no final do processo, em que todos
       os elementos da lista forem examinados, eh retornado todos os
       divisores dela.

       list, int -> list)'''
    
    qntNum = len(listaNum)
    cont = 0
    numDivisiveis = []

    while cont < qntNum:
        if listaNum[cont]%num == 0:
            numDivisiveis.append(listaNum[cont])
        cont += 1
    return numDivisiveis