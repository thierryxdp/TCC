def qtd_divisores(numero):
    '''Função que retorna quantos divisores um numero possui'''
    dibisores = []
    QtDibisores = 0
    dibisoresPossibeis= list(range(1,numero+1))
    
    for dibisor in dibisoresPossibeis:
        if numero%dibisor == 0:
            dibisores.append(dibisor)
    QtDibisores = len(dibisores)
    return QtDibisores