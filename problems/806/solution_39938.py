#Esta função verifica se dois retângulos vão se colidir, as coordenadas devem ser passadas em tuplas de forma que fique no retangulo 1 x_inf_esq1y_inf_esq1x_sup_dir1y_sup_dir1 e no retangulo 2 fique x_inf_esq2y_inf_esq2x_sup_dir2y_sup_dir2
#tuple,tuple -> bool
def colisao(ret1,ret2):
	x_inf_esq1 = ret1[0:1]
	y_inf_esq1 = ret1[1:2]
	x_sup_dir1 = ret1[2:3]
	y_sup_dir1 = ret1[3:4]
	x_inf_esq2 = ret2[0:1]
	y_inf_esq2 = ret2[1:2]
	x_sup_dir2 = ret2[2:3]
	y_sup_dir2 = ret2[3:4]
	if x_inf_esq1 > x_sup_dir2:
		return (False)
	elif x_inf_esq1 <= x_sup_dir2 and y_inf_esq1 > y_sup_dir2:
		return (False)
	elif y_inf_esq1 > y_sup_dir2:
		return (False)
	elif y_inf_esq1 <= y_sup_dir2 and x_inf_esq1 > x_sup_dir2:
		return (False)
	elif x_inf_esq2 > x_sup_dir1:
		return (False)
	elif x_inf_esq2 <= x_sup_dir1 and y_inf_esq2 > y_sup_dir1:
		return (False)
	elif y_inf_esq2 > y_sup_dir1:
		return (False)
	elif y_inf_esq2 <= y_sup_dir1 and x_inf_esq2 > x_sup_dir1:
		return (False)
	else:
		return(True)