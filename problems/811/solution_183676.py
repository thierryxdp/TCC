def colchao(media,H,L):
    '''funcao que retorna True se o colchao consegue
    passar pela porta e False caso ele nao passe, dado 
    as medidas do colchao e da porta em centimetros
    list,int,int->bool'''
    
    [A,B,C]= media
    
    if B<=H:
        return True
    else:
        return False