# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao (medidas,H,L):
    "Função que recebe uma lista com os valores das dimensões da porta da casa de João e as dimensões do colchão que ele quer comprar"
	"Retorna um booleno dizendo se passa ou não da porta"
    "list, int, int -> bool"
    
    if (medidas[1] <= H <= medidas[2] or medidas[1] < L):
        return True
    else:
        return False