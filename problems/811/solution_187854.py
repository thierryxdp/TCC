def colchao(medidas,h,l):
    'dado as dimensoes do colchao, altura da porta e largura. retorna true se passar da porta e false se nao passar. list, float, float -> Boolean'
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if a<=l and c<=h:
        return True 
    elif b<=l and c<=h:
        return True
    elif c<=l and b<=h:
        return True
    elif a<=l and b<=h :
        return True 
    elif c<=l and a<=h:
        return True 
    elif b<=l and a<=h:
        return True 
    else:
        return False