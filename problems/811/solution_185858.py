def colchaopassa(medidascolchao, h, l):
    '''Função que recebe as medidas de um colchão e a altura e
largura da porta e retorna se o colchão passa pela porta ou não.
Entradas:
    medidascolchao: list
    h, l: int
Saída:
    bool'''
    medidascolchao.sort()
    a,b,c = medidascolchao
    if (b > h and b > l):
        return False
    else:
        return True