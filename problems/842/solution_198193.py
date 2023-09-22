def pontos_por_time(lista):
    pts1 = [0]
    pts2 = [0]
    if lista[0[2[0,]]] == lista[0[2[1,]]]:
        pts1[0,] = 1
        pts2 [0,] = 1
    if lista[0[2[0]]] >= lista[0[2[1]]]: pts1[0,] = 3
    else: pts2[0] = 3
    if lista[1[2[0]]] == lista[1[2[1]]]:
        pts1[0] = int(pts1[0]) + 1
        pts2[0] = int(pts2[0]) + 1
    if lista[1[2[0]]] >= lista[1[2[1]]]:
        pts2[0] = int(pts2[0]) + 3
    else: pts1[0] = int(pts1[0]) + 3
    return [pts1, pts2]