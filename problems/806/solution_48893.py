#Start your python function here
def colisao(ret1,ret2):
    t=[ret1,ret2]
    if t[0]>t[6] or t[2]<t[4] or t[1]>t[7] or t[3]<t[5]:
        return "False"
    else: 
        return "True"
            
        
           
   

     
     

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado