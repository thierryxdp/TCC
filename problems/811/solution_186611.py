# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

colchao(medidas,H,L):
    """dado as dimensões de um colchão no formato de um paralelepípedo reto ratângulo
    que só uma face será  arrastada no chão,
    as dimensões de altura e largura da porta
    ele diz se é possível passar pela porta (true) ou não  (false)
    
    medidas:lista com as dimensões do colchão [A,B,C]
    H:altura da porta
    L:largura da porta
    
    exemplo:
    colchao([25,120,220],200,100)
    true
    
    entrada-> lista, float, float
    retorna-> bool"""
    
    
    Hcolchao= medidas[0]
    Lcolchao= medidas[1]
    Ccolchao= medidss[2]
    
    
    if Hcolchao> H:
        return not Hcolchao>H
    elif Hcolchao>L:
        return not Hcolchao>L
    elif Lcolchao>H:
        return not Lcolchao>H
    elif Lcolchao>L:
        return not Lcolchao>L
    elif Ccolchao>H:
        return not Ccolchao>H
    elif Ccolchao>L:
        return not Ccolchao>L
    else:
        1==1