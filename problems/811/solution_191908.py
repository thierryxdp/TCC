# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas, H, L):
    maior_lado = max(medidas)
    medidas.remove(maior_lado)
    maior_que_H = False
    maior_que_L = False
    
    for x in medidas:
        if(x > H and maior_que_H == False):
            maior_que_H = True
        elif(x > L and maior_que_L == False):
            maior_que_L = True
    
    resultado = maior_que_H & maior_que_L 
	return ~resultado