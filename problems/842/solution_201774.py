def pontos_por_time(rodada):
    if rodada[0][2][0]==rodada[0][2][1] and rodada[1][2][0]==rodada[1][2][1]:
        pontos_fla=2 
        pontos_cor=2
    if rodada[0][2][0]==rodada[0][2][1] and rodada[1][2][0]<rodada[1][2][1]:
        pontos_fla=4  
        pontos_cor=1
    if rodada[0][2][0]==rodada[0][2][1] and rodada[1][2][0]>rodada[1][2][1]:
        pontos_fla=1 
        pontos_cor=4
    if rodada[0][2][0]<rodada[0][2][1] and rodada[1][2][0]>rodada[1][2][1]:
        pontos_fla=0 
        pontos_cor=6
    if rodada[0][2][0]<rodada[0][2][1] and rodada[1][2][0]<rodada[1][2][1]:
        pontos_fla=3 
        pontos_cor=3
    if rodada[0][2][0]<rodada[0][2][1] and rodada[1][2][0]==rodada[1][2][1]:
        pontos_fla=1 
        pontos_cor=4
    if rodada[0][2][0]>rodada[0][2][1] and rodada[1][2][0]<rodada[1][2][1]:
        pontos_fla=6 
        pontos_cor=0
    if rodada[0][2][0]>rodada[0][2][1] and rodada[1][2][0]==rodada[1][2][1]:
        pontos_fla=4 
        pontos_cor=1
    if rodada[0][2][0]>rodada[0][2][1] and rodada[1][2][0]>rodada[1][2][1]:
        pontos_fla=3 
        pontos_cor=3
    Pontos={rodada[0][0]:pontos_fla,rodada[0][1]:pontos_cor}
    return Pontos