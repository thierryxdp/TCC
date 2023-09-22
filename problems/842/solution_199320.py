def pontos_por_time (lista):
    '''list -> dict'''
    pt_ida, pt_volta = lista[0],lista[1]
    pts = {pt_volta[0]:0, pt_volta[0]:1}
    #EMPATES
    if pt_ida[2][0] == pt_ida[2][1]:
        pts_ida[2][0] = pts_ida[2][0] + 1
		pts_ida[2][1] = pts_ida[2][1] + 1
	
    if pt_volta[2][0] == pt_volta[2][1]:
        pts_volta[2][0] = pts_volta[2][0] + 1
        pts_volta[2][1] = pts_volta[2][1] + 1
        
    if pt_ida[0][0] < pt_ida[1][0]:
        pts[pt_ida[1]] = pts[pt_ida[1]] + 3
    if pt_ida[0][0] > pt_ida[1][0]:
        pts[pt_ida[0]] = pts[pt_ida[0]] + 3
   
	if pt_volta[0][0] < pt_volta[1][0]:
        pts[pt_volta[1]] = pts[pt_volta[1]] + 3
    if pt_volta[0][0] > pt_volta[1][0]:
        pts[pt_volta[0]] = pts[pt_volta[0]] + 3
        
	return pts