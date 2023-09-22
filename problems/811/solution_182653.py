def colchao(medidas,H,L):
    '''dado a lista com as medidas do colchao e a altura H e largura L daa porta, retorna true caso o colchao passe pela porta e false caso contrario
lista,int,int->bool'''
    a = medidas[0] 
    b = medidas[1] 
    c = medidas[2] 
    
    return H>=b or H>=c or L>=b or L>=c