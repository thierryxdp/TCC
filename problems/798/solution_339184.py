# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(a):
	conjunto = str.split(a)
    
    for i in conjunto:
        total = str.count(i,conjunto)
    return total