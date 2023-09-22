def faltante(l):
    '''essa funcao recebe uma lista com todos os numeros inteiros de 1 a N,nao necessariamente
    em ordem crescente, e com um numero da sequencia faltando, a funcao retorna o numero que estava faltando
    list-->int'''
    list.sort(l)
    l1=list(range(1,l[-1]+1)
    i=0
    while(i<len(l)):
        if(l[i]!=l1[i]):
            break
        i+=1
    return l1[i]