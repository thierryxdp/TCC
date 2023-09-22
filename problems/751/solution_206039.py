# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	frase_sem_espacos = frase.strip() #Elimina os espaços do final e inicio da string
	palavras = frase_sem_espacos.split() #Divide as palavras da string
    return len(palavras)