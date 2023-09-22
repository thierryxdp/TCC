def repetidos(numeros):
    lista_numeros_unicos = []
    for numero in lista:
        if(numero in lista_numeros_unicos): #Verifica se o atual elemento existe na lista original
            pass #Se existir não faz nada
        else:
            lista_numeros_unicos.append(numero) #Se não existir, adiciona com o comando append() o numero na lista
    return lista_numeros_unicos