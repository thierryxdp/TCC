#porta h x L 
#colcao a x b x c
#uma das faces paralelas ao chao na entrada
#entrada: lista com abc do menor p maior e HL
def colchao(medidas,h,l):
    if medidas[2] <=h or medidas[1]<= l or medidas [1]<= h:
        return True
    else:
        return False