def dimensaoporta(h,l):
    '''Essa função arruma a assimetria da porta;
    Recebe altura x largura;
    Retorna o valor corretor da porta '''
    if h >= l:
        return (h,l)
    else :
        return (l,h)
        
def colchao(m,h,l):
    '''Essa Função calcula se medidas do colchao permite que ele passe pela medida da porta;
    Recebe os parametros do colchão e a porta;
    Retorna True se o colchao passa pelas portas e Flase caso contrario.'''
    m1 = list.sort(m)
    n = dimensaoporta(h,l) 
    if m[1] > n[0] or m[0] > n[1]:
        return 'False'
    else :
        return 'True'