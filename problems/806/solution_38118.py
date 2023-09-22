#Start your python function here
def colisao(ret1,ret2):
    rect1_x = ret1[:1]#define o x
    rect1_y = ret1[2:3]#define o y
    rect1_width = ret1[4:5]#define a largura
    rect1_height = ret1[6:7]#define a altura

    rect2_x = ret2[:1]#define o x do ret2
    rect2_y = ret2[2:3]#define o y do ret2
    rect2_width = ret2[4:5]#define a largura
    rect2_height = ret2[6:7]#define a altura
	##detecta colisão de 2 retangulos
    if (rect1_x < rect2_x + rect2_width and
            rect1_x + rect1_width > rect2_x and
            rect1_y < rect2_y + rect2_height and
            rect1_y + rect1_height > rect2_y):

        return True

    else:

        return False