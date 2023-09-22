# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
'''
   funcao que recebe uma frase e retorna a quantidade de palavras dessa frase
   str -> float
   '''
#quando eu testo no shell da certo, mas aki esta dando erro
	lista = frase[1:-1].split(' ')
    lista1 = len(lista)
    return lista1