#Start your python function here
def colisao( ret1, ret2):
    ''' a função colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
        coordenadas dos vertices inferior esquerdo ecsuperior esquerdo do primeiro retâangulo e do segundo
        retângulo, nessa ordem, e devolve True se ha colisao entre 2 retângulos e False, caso contraio.
        tuple, tuple --> bool '''
    
   # primeira etapa - extrair as coordenadas das tuplasrecebidas como argumentos
       xie1, yie1, xsd1, ysd1 = ret1
       xie2, yie2, xsd2, ysd2 = ret2
   # segunda etapa - calculo do resultado
       if xie2 > xsd1 or xie1 > xsd2 or yie1 > ysd2 or yie2 > ysd1:
           return 0 != 0
        else:
            return 0 == 0