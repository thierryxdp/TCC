def qtd_divisores(n):
    '''Função que retorna o numero de divisores que um 
    numero(n) possui. int -> int '''
    lista = []
    for x in list(range(1,n+1)):
                  if n%x == 0:
                      lista = lista + [x]
    return len(lista)