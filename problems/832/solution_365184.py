def eh_quadrada(matriz):
    """Calcula e retorna se a matriz eh quadrada, sem nenhuma linha, nem coluna; list--> bool"""
    for i in matriz:
        for j in i:
            if range(j) != len(matriz):
                print(range(j))
                return False
        		
    return True