def colchao(medidas,h,l):
    '''
    Função que retorna se um colchão passa ou não pela porta 
    dados, respectivamente, as medidas dos colchão em forma
    de lista crescente, e a altura e largura da porta 
    (todos em cm)
    '''
    if (medidas[2]>h and medidas[2]>l) and (medidas[1]>h and medidas[1]>l):
        return False
    else:
        return True