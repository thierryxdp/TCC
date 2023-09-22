def colchao(medida,H,L):
    '''funcao que retorna true se o colchao consegue 
    passar pela porta e false caso ele nao passe
    list,int-> bool'''
    [A,B,C] =medida
    if B<=H:
        return True 
    else:
        return False