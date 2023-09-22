# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que, dadas de entrada as dimensoes (tamanhos interios em cm) de
       um colchao (altura, largura e comprimento) e as de uma porta (altura e largura),
       retorna True se esse colchao passa através da porta e False se não.
       list, int, int - > bool"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if ((B<=L and A<=H) or (B<=H and A<=L)) or ((C<=L and A<=H) or (C<=H and A<=L)) or ((C<=L and B<=H) or (C<=H and B<=L)):
    #       deitado         em pe                   deitado                 em pe           em pe em b      em pe em c
    	return True
    else:
        return False

#casos de teste:
#colchao([50,150,200],230,120) == True
#colchao([30,190,220],180,140) == False
#colchao([40,130,205],210,130) == True