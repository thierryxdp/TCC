def colchao(medidas,H,L):
    'Retorna true para as medidas do colchao que passa pela porta e falso caso as medidas n passem'
    'list,int,int----bool'
    largura_colchao=medidas[0]
    comprimento_colchao=medidas[1]
    alturacolchao=medidas[2]
    if H>L:
        maioraresta=H
        menoraresta=L
    else:
        maioraresta=L
        menoraresta=H
    if largura_colchao and comprimento_colchao<maioraresta:
        return True
   
    else:
        return False