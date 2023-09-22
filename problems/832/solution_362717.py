def eh_quadrada(matriz):
    "Funcao que indica se uma matriz eh quadrada ou não"
	"list -> bool"
    for i in matriz:
        if len(matriz) != len(i):
            return False
    return True