def eh_quadrada(n):
    "funcao que identifica se uma matriz e quadrada"
    if len(n) == 0:
         return True
    for i in range(len(n)):
        for j in range(len(n[0])):
                if len(n) == len(n[0])):
                    return True
    return False