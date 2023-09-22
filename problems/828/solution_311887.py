def primo(n):
    '''Função que, dado um número inteiro positivo, verifica se este número é primo
ou não. Retorna a resposta em forma de booleano
    int -> bool
    '''
    if n%2==0 and n>2:
        return False
    divisores=[1,n]
    for i in range(2,n//2):
        if n%i==0:
            list.append(divisores,i)
    if len(divisores)==2:
        return True
    else:
        return False