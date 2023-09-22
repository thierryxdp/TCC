def pontos_por_time(x):
    return pontos_por_time[0][0]+":"+pontosxi+pontosxv+","+pontos_por_time[0][1]+":"+pontosyi+pontosyv

def pontosxi(x):
    if pontos_por_time[0][2][0]>pontos_por_time[0][2][1]:
    	return pontos_por_time[0][2][0]*3
	if pontos_por_time[0][2][0]==pontos_por_time[0][2][1]:
        return pontos_por_time[0][2][0]*1 
def pontosxv(x):
    if pontos_por_time[1][2][1]>pontos_por_time[1][2][0]:
        return pontos_por_time[1][2][1]*3
    if pontos_por_time[1][2][1]==pontos_por_time[1][2][0]:
        return ppontos_por_time[1][2][1]*1
    
def pontosyi(x):
    if pontos_por_time[0][2][1]>pontos_por_time[0][2][0]:
        return pontos_por_time[0][2][1]*3
    if pontos_por_time[0][2][0]==pontos_por_time[0][2][1]:
        return pontos_por_time[0][2][1]*1

def pontosyv(x):
    if pontos_por_time[1][2][0]>pontos_por_time[1][2][1]:
        return pontos_por_time[1][2][0]*3
    if pontos_por_time[1][2][1]==pontos_por_time[1][2][0]:
        return pontos_por_time[1][2][0]