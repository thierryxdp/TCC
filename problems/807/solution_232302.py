def conta_frases(x):
    '''a função recebe um texto e retorna o numero de frases que aparecem no texto
    assinatura: str -> int
    casos de teste:
    conta_frases('preciso tirar um cochilo. Meu deus! que horas são? vou perder a minha aula...') == 4
    conta_frases('eu adoro comer!') == 1
    '''

    x1 = str.count(x,'.')
    x2 = str.count(x, '!')
    x3 = str.count(x, '?')
    x4 = str.count(x, '...')

    if x4 == 0:
        return x1+ x2 + x3
    elif x4 > 0:
        return x2 + x3 + x4 + x1- (3*x4)