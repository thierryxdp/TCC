def colisao(ret1x1,ret1y1,ret1x2,ret1y2,ret2x1,ret2y1,ret2x2,ret2y2):
	'''A função colisao verificará, através das coordenadas cartesianas, a existência ou não de
colisão entre dois retângulos.
Caso a função retorne "Verdadeiro" (True), significa que os dois retângulos colidem! Caso o
contrário, não haverá colisão (False)
float, float, float, float, float, float, float, float -> Bool'''

resultado = not (ret2x2 < ret1x1 or ret1x2 < ret2x1) and not (ret2y2 < ret1y1 or ret1y2 <
ret2y1)
return resultado