def maiores(numeros_inteiros,n):
        '''função que, dada uma lista
        retorna a lista, apos o n, em ordem crescente
        lista,int -> list'''
        if n in numeros_inteiros:
            list.remove(numeros_inteiros,n)
        list.insert(numeros_inteiros,-1,n)
        list.sort(numeros_inteiros)
        return numeros_inteiros[list.index(numeros_inteiros,n)+1:]