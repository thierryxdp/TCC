def melhor_volta(matriz):
	
#retorna uma tupla com quem deu a volta mais rapida, qual o tempo da volta e em qual volta, dado uma matriz    
    
    lista = []


    for l in range(0, 6):
        lista.append(min(matriz[l]))

    indice = lista.index(min(lista))
    linha = matriz[indice]

    return (lista.index(min(lista))+1, min(lista), linha.index(min(linha))+1)