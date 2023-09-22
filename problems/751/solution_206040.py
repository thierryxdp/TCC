# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	frase1 = frase.strip() #Elimina os espaços do final e inicio da string
	palavras = frase1.split() #Divide as palavras da string
    return len(palavras)