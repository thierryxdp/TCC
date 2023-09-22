def intercala(abc,xyz):
    '''Retorna o valor de L3 de acordo com os valores intercalados de L1 e L2
lista, lista -> lista'''
    L1 = [abc]
    L2 = [xyz]
    a = L1[0][0] 
    b = L1[0][1]
    c = L1[0][2]
    x = L2[0][0] 
    y = L2[0][1] 
    z = L2[0][2]
    
    L3 = ['a'+'x'+'b'+'y'+'c'+'z']
    return L3