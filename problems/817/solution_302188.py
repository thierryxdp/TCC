def maiores(lista,N):
    '''Essa Funcao dada uma lista de numeros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n;
    Recebe uma lista de numeros e um numero inteiro n;
    Retorna outra lista, que contenha todos os numeros da lista original maiores que n.'''
    listafinal=[]
    for i in range(len(lista)):
        if(lista[i]>N):
            listafinal.append(lista[i])
    list.sort(listafinal)        
    return listafinal

def acima_da_media(notas):
    '''Essa Funcao ue dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média;
    Recebe uma lista com as notas dos alunos de uma turma;
    Retorna uma lista ordenada com as notas que ficaram acima da média.'''
    soma = sum(notas) 
    alunos = len(notas)
    media = soma/alunos   
    resultados = maiores(notas,media)
	return resultados