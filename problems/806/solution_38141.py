#Start your python function here
def colisao(ret1,ret2):
    x_ret1 = ret1[0]#eixo x inferior esquerdo do retangulo
    y_ret1 = ret1[1]#eixo y inferior esquerdo do retangulo
    ret1_width = ret1[2]#eixo x superior direito do retangulo
    ret1_height = ret1[3]#eixo y superior direito do retangulo
    x_ret2 = ret2[0]
    y_ret2 = ret2[1]
    ret2_width = ret2[2]
    ret2_height = ret2[3]
###calcula a colisao entre eles
    if (x_ret1 < x_ret2 + ret2_width and
        x_ret1 +  ret1_width > x_ret2 and
        y_ret1 < y_ret2  + ret2_height and
        y_ret1 + ret1_height > y_ret2):

    	return True
#se n ter uma,retorna que não aconteceu
    else:

        return False