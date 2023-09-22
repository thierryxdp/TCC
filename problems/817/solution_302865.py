def maiores(inteiros, n):
    ''' recebe uma lista e um numero inteiro n e retorna uma lista com os valores da
    lista original com valores maiores que n e em ordem crescente'''
    
    list.append(inteiros, n) #une n à lista inteiros
    list.sort(inteiros) #coloca a lista inteiros em ordem crescente
    repetido = list.count(inteiros, n) #verifica se n tem repetição na lista de inteiros
    i = list.index(inteiros, n) #indice de n na lista crescente
    lista = inteiros[(i + repetido):] #retira os valores repetidos de n e os numeros menores que ele

    return lista

def acima_da_media(lista_notas):
    '''recebe uma lista com notas de alunos de uma turma e retorna a lista ordenada com as notas acima da média'''
    list.sort(lista_notas)
    inteiros = lista_notas
    n = sum(lista_notas)/len(lista_notas)
    
    lista_final = maiores(inteiros, n)
    
    return lista_final