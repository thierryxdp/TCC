''' nessa questao, eu recebo uma lista com a uma certa 
quantidade de notas dos alunos de uma turma. 
Para descobrir a quantidade de elementos, preciso usar
1) len(notas); depois disso, preciso somar os elementos 
dessa lista e dividir pela sua quantdade de termos 
(achado em len(notas)) -- para isso uso o 2)sum(lista)/len(notas)
3)depois eu utilizo a funcao da questao 6 para separar 
apenas as notas maiores que a média em uma lista ordenada'''

def maiores(lista_numeros,n): #funcao da questao 6
    '''Funcao que recebe de entrada uma lista de numeros 
    inteiros e um numero inteiro n e retorna outra 
    lista com todos os numeros da lista original
    maiores do que n em ordem crescente.
    list, int -> list'''
    lista_maiores = lista_numeros + [n]
    if n in lista_numeros:
        lista_maiores = lista_numeros
    list.sort(lista_maiores)
    return lista_maiores[list.index(lista_maiores,n)+1:]

def acima_da_media(notas):
    '''Funcao que recebe de entrada as notas, que variam 
    de 0.0 a 10.0, dos alunos de uma turma, e retorna 
    apenas aquelas maiores que média das notas de
    todos os alunos.
    list -> list'''
    media = sum(notas)/len(notas)
    return maiores(notas,media)

#casos de teste
#acima_da_media([1,5,6,9,10]) == [9, 10]
#acima_da_media([5,10,6.5,3.5,5,6]) == [6.5,10]