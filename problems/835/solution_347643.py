def melhor_volta(matriz):
    """Função que identifica o menor tempo de uma matriz
    e retorna uma tupla contendo as informações: de foi o menor tempo
    qual foi esse menor tempo e em que volta faz o n=menor tempo
    list -> tuple"""
    menores = []
    for i in matriz:
        menores.append(min(i))
    for i in matriz:
        for j in i:
            if j == min(menores):
                quem = matriz.index(i)+1
                tempo = j
                quando = i.index(j)+1
 	return (quem, tempo, quando)