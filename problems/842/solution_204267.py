def pontos_por_time (L1,L2):
	L1 = [["time1", "time2"], ["gol1","gol2"]]
	L2 = [["time2", "time1"], ["gol2","gol1"]]

if L1[1][0]==L1[1][1]:
	i1 = 1 
    i2 = 1
    
if  L2[1][0]==L2[1][1]:
    v1 = 1 
    v2 = 1

if L1[1][0]>L1[1][1]:
    i1 = 3
    i2 = 0

if L1[1][0]<L1[1][1]:
    i1 = 0
    i2 = 3
    
if  L2[1][0]>L2[1][1]:
    v1 = 0
    v2 = 3
    
if L2[1][0]<L2[1][1]:
    v1 = 3
    v2 = 0
    
pontost1 = i1 + v1

pontos2 = i2 + v2

fase1 = { L1[0][1]: pontos1, L1[0][1]:pontos2}
	return fase1