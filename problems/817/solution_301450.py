def acima_da_media(notas_turma)
	'''
    funcao que recebe uma lista com notas da turma e retorna quem
    ficou com a nota acima da media
    '''

	media_acima = sum(notas_turma)
    media_todos = len(notas_turma)
    media_aprovados = media_acima/media_todos
    return maiores(notas_turma,media_aprovados)

def maiores(lista_numint,n):
	'''
    funcao que recebe uma lista com numeros inteiros 
    e um numero inteiro n e retorna outra lista com os 
    numeros inteiros maiores do que n em ordem crescente
    
    list, int -> list
    '''

	nova_lista=([i for i in lista_numint if i > n])
	return sorted (nova_lista)