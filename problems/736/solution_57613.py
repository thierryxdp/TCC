def concatenacao(a, b):
    '''concatena duas strings 'a' e 'b' juntando-as
    assinatura: str,str > str
    casos de teste: concatenacao('abc','de') ==abcdedeabc
    concatenacao('oLobo','AmaoBolo') ==oLoboAmaoBoloAmaoBolooLobo
    concatenacao('22/02/','2022/') ==22/02/2022/2022/22/02/'''
    return str(a) + str(b) + str(b) + str(a)