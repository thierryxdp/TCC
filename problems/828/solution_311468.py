def qtd_divisores(n):
    '''Função que, dado um número inteiro n, conte quantos divisores ele tem
    int -> int
    '''
    divisores = [n]
    for a in range(n//2):
        if n%(range(1,n//2+1)[a])==0:
            list.append(divisores,range(1,n//2+1)[a])
    resposta = len(divisores)
    return resposta

def primo(n):
    '''Função que, dado um número inteiro positivo, verifica se este número é primo
ou não. Retorna a resposta em forma de booleano
    int -> bool
    '''
    if qtd_divisores(n)==2:
        return True
    else:
        return False