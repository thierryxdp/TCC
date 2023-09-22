# Função que intercala as listas
def concatena_listas(a, b):
    temp = [a[0], b[0], a[1], b[1], a[2], b[2]]

    return temp


# listas
L1 = [1,3,5]
L2 = [2,4,6]
LX = [7,9,11]
LY = [8,10,12]

# print das chamadas com exemplos teste
L3 = concatena_listas(L1, L2)
print(L3)
L3 = concatena_listas(LX, LY)
print(L3)
L3 = concatena_listas(L1, LY)
print(L3)
L3 = concatena_listas(L2, LX)
print(L3)