def colchao(x,y,z):
    '''Função que dada as dimensões de um colchão, retorna se é possível passar pela porta da casa dada as dimensões da porta
       list,int,int->booleanos'''
    x.sort()
    if x[-2]<=y and x[-3]<=z and y>=z:
        return 'true'
    elif x[-2]<=z and x[-3]<=y and z>=y:
        return 'true'
    else: 
        return 'false'