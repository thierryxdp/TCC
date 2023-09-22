def faltante(l):
        '''Recebe uma lista de tamanho n-1 contendo apenas numeros inteiros nao 
        repetidos de 1 a n e retorna o numero inteiro que pertence ao intervalo
        [1,N] mas que esta faltando na lista de entrada;
        list -> int'''
        list.sort(l)
        cnt=0
        lista=list(range(len(l)+1))[1:]
        if lista == l:
            return l[-1]+1
        while lista[cnt] == l[cnt]:
            cnt=cnt+1
        if lista[cnt] != l[cnt]:
            return lista[cnt]