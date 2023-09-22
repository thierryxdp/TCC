def colisao(ret1,ret2):
# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
	ret1 = (x1, y1, x11, y11)
	ret2 = (x2, y2,  x22, y22)
    ret1, ret2 -> bool
# segunda etapa - calculo do resultado
if([x2]>[x11]): return true
if([y2]>[y11]): return true
if([x1]>[x22]): return true
if([y1]>[y22]): return true
else: return false