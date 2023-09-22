def melhor_volta(matriz):
    """Funcao que calcula a melhor volta dentre os corredores retornando
    o tempo dela e em qual volta foi
    list --> tupla"""
    checktup = ()
    checklist = []
    for i in range(len(matriz)):
        i = -1
        x = list.pop(matriz, i)
        checklist = checklist + x
        checktup = checktup + y
    z = min(checktup)
    w = list.index(checklist, z) + 1
    if w/10 <= 1:
        return 1, z, w 
    if 1 < w/10 <= 2:
        return 2, z, (w - 1) * 10 
    if 2 < w/10 <= 3:
        return 3, z, (w - 2) * 10
    if 3 < w/10 <= 4:
        return 4, z, (w - 3) * 10
    if 4 < w/10 <= 5:
        return 5, z, (w - 4) * 10
    if 5 < w/10 <= 6:
        return 6, z, (w - 5) * 10