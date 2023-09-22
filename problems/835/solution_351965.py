def melhor_volta(matriz):
    """Funcao que calcula a melhor volta dentre os corredores retornando
    o tempo dela e em qual volta foi
    list --> tupla"""
    checktup = ()
    checklist = []
    for i in range(len(matriz)):
        i = 0
        x = list.pop(matriz, i)
        for i in range(len(x)):
            i = 0
            w = list.pop(x, i) 
            checklist = checklist + [w]
            checktup = checktup + (w,)
    y = min(checktup)
    z = list.index(checklist, y) + 1
    if z/10 <= 1:
        return 1, y, z
    if 1 < z/10 <= 2:
        return 2, y, (z - 1) * 10 
    if 2 < z/10 <= 3:
        return 3, y, (z - 2) * 10
    if 3 < z/10 <= 4:
        return 4, y, (z - 3) * 10
    if 4 < z/10 <= 5:
        return 5, y, (z - 4) * 10
    if 5 < z/10 <= 6:
        return 6, y, (z - 5) * 10