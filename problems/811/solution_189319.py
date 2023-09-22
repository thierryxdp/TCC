#Questao 3
def colchao(medidas, H, L):
    '''
Funcao que dadas medidas de dimensoes, altura e largura
retornam se o colchao passa pelas portas ou nao.
str, int
    '''
    medidas_ordenadas= medidas[0],medidas[1],medidas[2]
    portao= max(L, H)
    
    if medidas[1] <=L or medidas[1] <=H:
        return True 
    if medidas[1] >=L or medidas[1] >=H:
        return False