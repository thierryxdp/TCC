def colchao(m,h,l):
    '''Essa Função calcula se medidas do colchao permite que ele passe pela medida da porta;
    Recebe os parametros do colchão e a porta;
    Retorna True se o colchao passa pelas portas e Flase caso contrario.'''
    m1 = list.sort(m)
    n = (h,l) 
    if m[1] > n[0] or m[0] > n[1]:
        return 'False'
    else :
        return 'True'