def pontos_por_time (lista):
    '''Função que recebe uma lista contendo o saldo de gols
    de duas partidas e retorna a soma dos pontos corridos
    list -> dict'''
    pt_ida, pt_volta = lista[0],lista[1]
    pts = {pt_volta[0]:0, pt_volta[1]:0}
    #EMPATES
    if pt_ida[2][0] == pt_ida[2][1]:
		pts[pt_ida[0]] = pts[pt_ida[0]] + 1
		pts[pt_ida[1]] = pts[pt_ida[1]] + 1
	
    if pt_volta[2][0] == pt_volta[2][1]:
        pts[pt_volta[1]] = pts[pt_volta[1]] + 1
        pts[pt_volta[0]] = pts[pt_volta[0]] + 1
        
    if pt_ida[2][0] < pt_ida[2][1]:
        pts[pt_ida[1]] = pts[pt_ida[1]] + 3
    if pt_ida[2][0] > pt_ida[2][1]:
        pts[pt_ida[0]] = pts[pt_ida[0]] + 3
   
	if pt_volta[2][0] < pt_volta[2][1]:
        pts[pt_volta[1]] = pts[pt_volta[1]] + 3
    if pt_volta[2][0] > pt_volta[2][1]:
        pts[pt_volta[0]] = pts[pt_volta[0]] + 3
        
	return pts