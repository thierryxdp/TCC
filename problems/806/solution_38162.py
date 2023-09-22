def colisao(ret1,ret2):
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    rect1_x = ret1[:1]
    rect1_y = ret1[2:3]
    rect1_width = ret1[4:5]
    rect1_height = ret1[6:7]
    rect2_x = ret2[:1]
    rect2_y = ret2[2:3]
    rect2_width = ret2[4:5]
    rect2_height = ret2[6:7]
    if(rect1.x < rect2.x + rect2.width &&
   rect1.x + rect1.width > rect2.x &&
   rect1.y < rect2.y + rect2.height &&
   rect1.y + rect1.height > rect2.y)
        return True
    else:
        return False