def colchao(medidas,H,L):
    ''' Função que recebe uma lista medidas de parâmetro 
        a(altura),b(largura), e c(comprimento), referente
        a um colchão. Essa função colchao também receberá 
        dois parâmetros H e L referente a altura e largura 
        da porta no qual o colchão passará. A função retorna
        True caso o colchão consiga passar pela porta, e False
        caso o colchão não passe pela porta.
    '''
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    if (b<=H and c>L) or (b>H and c<L):
        return True
    else:
        return False