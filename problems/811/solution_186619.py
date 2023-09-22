# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas,H,L):
    """dado as dimensões de um colchão no formato de um paralelepípedo reto ratângulo
    que só uma face será  arrastada no chão,
    as dimensões de altura e largura da porta
    ele diz se é possível passar pela porta (true) ou não  (false)
    
    medidas:lista com as dimensões do colchão [A,B,C] use para A a menor dimensão do colchão 
    H:altura da porta
    L:largura da porta
    
    exemplo:
    colchao([25,120,220],200,100)
    true
    
    entrada-> lista, float, float
    retorna-> bool"""
    
    
    Hcolchao= medidas[0]
    Lcolchao= medidas[1]
    Ccolchao= medidas[2]
    
    
    if Lcolchao<=H and L>Hcolchao:
        return Lcolchao <H
    elif Lcolchao <=L and H> L:
        return lcolchao <L
    elif Ccolchao <=H and L>Hcolchao:
        return Ccolchao <H
    elif Ccolchao <=H and L>Hcolchao:
        return Ccolchao <H
    else:
        return Lcolchao <H