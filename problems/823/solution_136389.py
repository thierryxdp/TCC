def faltante(lista):
    '''Função que ajuda Joãozinho a descobrir a peça faltando.
    Sabendo que o quebra-cabeças tem N peças numeradas de 1 a N
    e que só uma está faltando, a função faltante recebe como
    entrada uma lista com N-1 inteiros numerados e retorna o número
    faltando.list->int'''
    i=0
    n=1
    while lista[i]-lista[n]!= 1:
        n+=1
    if lista[i]-lista[n]==1:
        i+=1
        n=0
    return lista[i]