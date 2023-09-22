"""recebe uma tupla com quatro elementos e retorna apenas os elementos pares da tupla
x, s, y, z ->int
int, int, int, int ->int"""
def filtra_pares(x,s,y,z):
    t = [x, s, y, z]
    p=[]
    for valor in t:
        if valor % 2 ==0:
            p.append(valor)