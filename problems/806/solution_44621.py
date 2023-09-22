#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    #x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
   # x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
	var ret1 = {x: 5, y: 5, width: 50, height: 50}
	var ret2 = {x: 20, y: 10, width: 10, height: 10}

	if (ret1.x < ret2.x + ret2.width &&
   		ret1.x + ret1.width > ret2.x &&
   		ret1.y < ret2.y + ret2.height &&
   		ret1.y + ret1.height > ret2.y) {
    // collision detected!
}

// filling in the values =>

	if (5 < 30 &&
    	55 > 20 &&
    	5 < 20 &&
    	55 > 10) {
    // collision detected!
}