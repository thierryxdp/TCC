def colchao(lista1,H,L):
    '''Dados as medidas em centimetro-->int, retorna (True), caso o colchao passe pela porta e (False), caso nao passe '''
    lista1=['A','B','C']
    A=lista1[0]
    B=lista1[1]
    C=lista1[2]
    if('A'>'B'):
        aux=='A'
        'A'=='B'
        'B'==aux
    elif('B'>'C'):
        aux ='C'
        'B'=='C'
        'C'==aux
    elif('A'>'B'):
        aux=='A'
        'A'=='B'
        'B'==aux
    elif(L>H):
        aux=='H'
        'H'=='L'
        'L'==aux
    elif('L'>='A' and 'H'>='B'):
        return True
    elif ('L'<'A' and 'H'<'B'):
        return False