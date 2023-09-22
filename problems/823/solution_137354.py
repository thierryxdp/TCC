def faltante(N):
    '''Função que sabendo que o quebra-cabeça ̧tem N peças, numeradas de 1 a N e que exatamente uma está faltando, retorna qual peça está faltando, a função recebe uma lista de tamanho N − 1 contendo números inteiros (não repetidos) de 1 a N.
    lista[int]->int'''
    numerodetermos=len(N)+1
    y=N[-1:]
    soma=sum(y)+1
    total=(soma*numerodetermos)//2
    total2=sum(N)
    re=total-total2
    if re not in N:
        return re
    else:
        return sum(N[-1:])+1