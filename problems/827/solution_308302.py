def qtd_divisores(n):
    '''
    Recebe um número (n) qualquer. Inicia o contador (c) 
    com o número 1. E abre a lista dos divisores (d).
    Usa o while: caso o resto da divisão de c por n seja 0,
    então adiciona esse número na lista e soma 1 ao contador.
    Repete o processo até que o contador alcance o valor desejado.
    Feito isso, verifica a quantidade (q) de divisores 
    na lista e retorna essa quantidade.
    '''
    c = 1; d = []
    while c <= n:
        if n%c == 0: d.append(c)
        c += 1
	q = len(d)
    return q