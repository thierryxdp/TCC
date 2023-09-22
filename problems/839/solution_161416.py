def carros(np,cv=5):
    """calcular e retornar o número exato de carros necessários para esta viagem, considerando 
    que seja dado como entrada o número de pessoas.
    int , int -> int"""
    if (np//cv) == 0:
        return int(np/cv)
    else:
        return int(np/cv)+1