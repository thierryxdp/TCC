def colisao(coordenadas_ret_1,coordenadas_ret_2):
    """Função que retorna se houve colisão entre 2 retângulos dadas as suas coordenadas x e y,
    sendo estas respectivamente, x_inferior_esquerdo,y_inferior_esquerdo,
    x_superior_direito e y_superior_direito; tuple,tuple -> bool"""
    
    x_inf_esq1=coordenadas_ret_1[0]
    y_inf_esq1=coordenadas_ret_1[1]
    x_sup_dir1=coordenadas_ret_1[2]
    y_sup_dir1=coordenadas_ret_1[3]
    x_inf_esq2=coordenadas_ret_2[0]
    y_inf_esq2=coordenadas_ret_2[1]
    x_sup_dir2=coordenadas_ret_2[2]
    y_sup_dir2=coordenadas_ret_2[3]
	return not(x_sup_dir1<x_inf_esq2 or x_sup_dir2<x_inf_esq1 or y_sup_dir1<y_inf_esq2 or y_sup_dir2<y_inf_esq1)