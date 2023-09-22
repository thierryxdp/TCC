def pontos_por_time (lista1, lista2):
    '''list -> dict'''
    pt_ida = lista[0]
    pt_volta = lista[1]
    pts = {pt_ida[0]:0,pt_ida[1]:0}
    
	if pt_ida[0][0] > pt_ida[1][0]:
        pts[pt_ida[0]] = pts[pt_ida[0]] + 3
    if pt_ida[0][0] < pt_ida[1][0]:
        pts[pt_ida[1]] = pts[pt_ida[1]] + 3
    if pt_ida[0][0] == pt_ida[0][1]:
        pts_ida[0][0] = pts_ida[0][0] + 1
        pts_ida[1][0] = pts_ida[1][0] + 1
   
	if pt_volta[0][0] < pt_volta[1][0]:
        pts[pt_volta[1]] = pts[pt_volta[1]] + 3
    if pt_volta[0][0] > pt_volta[1][0]:
        pts[pt_volta[0]] = pts[pt_volta[0]] + 3
    if pt_volta[0][0] == pt_volta[0][1]:
      	pts_volta[0][0] = pts_volta[0][0] + 1
        pts_volta[1][0] = pts_volta[1][0] + 1
return pts