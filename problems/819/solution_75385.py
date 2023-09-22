def descobrir_multiplos(x,y):
#Criada a função, foi atribuido duas variáveis, a do múltiplicador e a lista com seus possíveis múltiplos
    numero = x
    lista = y
#Lista vazia para que sejam colocados os múltiplos descobertos
    multiplos = []
    for i in lista:
#Resto zero é uma divisão inteira, logo é múltiplo e entra na nova lista
        if i % numero == 0:
            multiplos.append(i)
#Caso contrário, apenas não entra na lista
        else:
            pass
    return multiplos