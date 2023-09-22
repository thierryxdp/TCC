def maiores(l, n):
    '''Função que  dada uma lista de números inteiros e um número inteiro n, retorna uma lista com todos os elementos em ordem crescente maiores que o númeto inteiro'n'; list,int->list'''
    m=[]
    i=0
    while i<len(l):
        if l[i]>n:
            m.append(l[i])
    	i = i + 1
        
    return sorted(m,key=int)