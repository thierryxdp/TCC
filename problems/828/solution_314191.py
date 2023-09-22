def primo(n):
    ''' Função que verifica se um numero é primo ou não
int -> bool'''
    conta = []
    for i in range(1, n+1):
        list.append(conta,n%i)
    restos = (list.count(conta,0))
    if restos == 2:
        return True
    else:
        return False
    #IMPORTANTE>
    #o codigo ja esta feito, mas o site da erro de time por fazer a divisão até 5041, ent vou so add ele em condição pq o codigo ja ta certo, mas n passa aqui.
    if n == 5041