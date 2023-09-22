def pontos_por_time(lista):
    pts1 = [0]
    pts2 = [0]
    lista = [[time1, time2, golsida], [time2, time1, golsvolta]]
    if golsida[0,] == golsida[1,]:
        pts1[0,] = 1
        pts2 [0,] = 1
    if golsida[0] >= golsida[1]: pts1[0,] = 3
    else: pts2[0] = 3
    if golsvolta[0] == golsvolta[1]:
        pts1[0] = int(pts1[0]) + 1
        pts2[0] = int(pts2[0]) + 1
    if golsvolta[0] >= golsvolta[1]:
        pts2[0] = int(pts2[0]) + 3
    else: pts1[0] = int(pts1[0]) + 3
    return [pts1, pts2]