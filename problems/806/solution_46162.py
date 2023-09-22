#Start your python function here
def colisao(ret1,ret2):

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
  
    return (ret2[0]<=ret1[0] and ret2[1]<= ret1[1])or\
           (ret2[0]<=ret1[2] and ret2[0]<= ret1[3])or\
           (ret2[2]<=ret1[0] and ret2[3]<= ret1[1])or\
           (ret2[2]<=ret1[2] and ret2[3]<= ret1[3])