def eh_quadrada(matriz):
    """função recebe uma matriz, identifica se ela é quadrada e retorna a resposta em valores boolenaos.LIST->BOOL"""
    num=len(matriz)
    lista=[]
    if matriz==[]:
        return True
    for x in range(num):
        num2=len(matriz[x])
        list.append(lista,num2)
    if sum(lista)==(len(matriz[0])**2):
        return True
    else:
        return False