def carros(a,b,c):
    '''retorna o número de carros necessários 
    para realizar uma viagem com certo número de pessoas(Np),
    sabendo que carros convencionais levam até 5 passageiros.'''
    x=math.ceil(a/2)
    y=math.ceil(b/3)
    z=math.ceil(c/5)
    return min(x,y,z)