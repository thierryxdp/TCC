# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	'''recebe uma frase e conta quantas palavras há naquela frase, sem contar os espaços
    str->int'''
	frase_sem_espacos =frase.split()
	return len(frase_sem_espacos)