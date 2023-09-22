#Start your pdef classificacao(cv, ce, cs, fv, fe, fs):
    '''verifica qual time se encontra melhor classificado na tabela de um campeonato,
    a função avalia a quantidade de vitória,empate e o saldo de gols.
    assinatura: int,int,int,int,int,int > str
    casos de teste: classificacao(10,4,5,10,4,4) ==Cormengo
    classificacao(10,2,1,11,0,2) ==Flaminthians
    classificacao(10,3,1,11,0,1) ==Empate'''
    if 3*cv + ce > 3*fv + fe:
        return 'Cormengo'
    elif 3*cv + ce < 3*fv + fe:
        return 'Flaminthians'
    elif 3*cv + ce == 3*fv + fe and cs > fs:
        return 'Cormengo'
    elif 3*cv + ce == 3*fv + fe and cs < fs:
        return 'Flaminthians'
    else:
        return 'Empate'