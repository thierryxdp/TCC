def primo(a):
    ''' Função que verifica se um numero é primo ou não
int -> bool'''
    lista = []
    for i in range(1, a+1):
        lista.append(a%i)
        r = (lista.count(0))
        #ideia: verificar a qnt de vezes que tem o zero na lista, se for duas vezes (divisivel por 0 e por ele mesmo), ent tem que ser primo
    if r == 2:
        return True
    else:
        return False