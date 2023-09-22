[23:41, 11/01/2022] Rodrigo Pereira: Blz
[23:42, 11/01/2022] Luciano Sara: # Função que intercala as listas
def intercala(a, b):
    temp = [a[0], b[0], a[1], b[1], a[2], b[2]]

    return temp


# listas
L1 = [1,3,5]
L2 = [2,4,6]
LX = [7,9,11]
LY = [8,10,12]

# print das chamadas com exemplos teste
intercala(L1, L2)
intercala(LX, LY)
intercala(L1, LY)
intercala(L2, LX)