def filtra_pares (tupla):

    a,b,c,d = tupla
    tupla_nova = ()

    if a % 2 == 0:
    
     tupla_nova = tupla_nova + (a,)

    if b % 2 == 0:

      tupla_nova = tupla_nova + (b,)

    if c %  2 == 0:

      tupla_nova = tupla_nova + (c,)

    if d % 2 == 0:

       tupla_nova = tupla_nova + (d,)


    return tupla_nova

def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado

    if (x < x2 and x > x2 and y < y2 and y > y2):
        
        return False
	
    if x_inf_esq1 > y_inf_esq2 and x_sup_dir1 > y_sup_dir2:

         return False

    else: 
	
     return True