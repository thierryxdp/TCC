# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)//2#corta a quantidade de caracteres na metade
    
    #retorna uma hashtag no inicio, segue a string do primeiro caractere
	#até a metade"x" e adciona outra hashtag
	#depois segue da metade até o fim e adciona outra hashtag
    return  '#'+(s[0:x])+'#'+(s[x:len(s)])+'#'