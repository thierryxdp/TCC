#Start your python function here

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
  def colisao(ret1,ret2):
        
    	x_inf_esq1 = int(ret1[0])
    	y_inf_esq1 = int(ret1[2])
    	x_sup_dir1 = int(ret1[4])
    	y_sup_dir1 = int(ret1[6])
    
    	x_inf_esq2 = int(ret2[0])
    	y_inf_esq2 = int(ret2[2])
    	x_sup_dir2 = int(ret2[4])
    	y_sup_dir2 = int(ret2[6])
    
    
    if (x_sup_dir1 - x_inf_esq2) > 0 and (x_sup_dir1 - y_inf_esq2) > 0 and (x_sup_dir2 - x_inf_esq1) > 0 and (y_sup_dir2 - y_inf_esq1) >0:
        return True
    
    else: 
        return False
    
    
    
    
   	

# segunda etapa - calculo do resultado