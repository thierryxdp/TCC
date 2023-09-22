def pontos_por_time(lista1):
    primeira=lista1[0]
    segunda=lista1[1]
    gol_pri=primeira[2]
    gol_seg=segunda[2]
    golA=gol_pri[0]
    golB=gol_pri[1]
    golAA=gol_seg[1]
    golBB=gol_seg[0]
    
    if golA>golB :
        golA=3
        golB=0
    if golA<golB:
        golA=0
        golB=3
    if golA==golB:
        golA=1
        golB=1   
    if golAA>golBB:
        golAA=3
        golBB=0
    if golAA<golBB:
        golAA=0
        golBB=3
    if golAA==golBB:
        golAA=1
        golBB=1 

     
        return {primeira[0]:golA+golAA,primeira[1]:golB+golBB}