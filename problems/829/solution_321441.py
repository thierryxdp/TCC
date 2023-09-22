def soma_h(n):
    '''Função que recebe um int(n) representando o número de termos de H;
Sendo H= 1+1/2+1/3+1/4+...+1/n, retorna o valor de h.
int->int'''
    s = 0
    for i in range(1,n+1):
        s = (s+1)/i
        if i<=n:
            s = round(s,2)
    return s