def qtd_divisores(n):
    c = 1; d = []
    while c <= n:
        if n%c == 0: d.append(c)
        c += 1
	q = len(d)
    return q

def primo(n):
    '''
    Usando a questão anterior, apenas verifiquei se a
    quantidade de divisores era igual a 2, sendo estes
    obrigatóriamente o número 1 e ele mesmo.
    '''
    d = qtd_divisores(n)
    if d == 2: return True
    else: return False