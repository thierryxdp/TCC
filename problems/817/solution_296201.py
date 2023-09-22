def acima_da_media(lista):
    def maiores(numeros_inteiros,n):
        '''retorna a lista, apos o n, em ordem crescente; lista,int -> list'''
        list.remove(numeros_inteiros,n)
        list.insert(numeros_inteiros,-1,n)
        list.sort(numeros_inteiros)
        return numeros_inteiros[list.index(numeros_inteiros,n)+1:]
    media_turma = sum(lista)/len(lista)
    return maiores(lista,media_turma)