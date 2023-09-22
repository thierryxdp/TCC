#Essa função serve para detectar e retornar números pares numa tupla de 4 itens
#tuple -> tuple
def par(x):
    return (x % 2) == 0

def impar(x):
    return not par(x)

"primeiramente definimos duas funções para identificar se o número é par ou não"

def filtra_pares(t):
    num = ()
    "definimos a função filtra pares, e adicionamos uma tupla vazia qualquer, para ser utilizada"
    if par(t[0]):
        num = num + (t[0],)
    if par(t[1]):
        num = num + (t[1],)
    if par(t[2]):
        num = num + (t[2],)
    if par(t[3]):
        num = num + (t[3],)
    "fazemos uma série de condicionais com o objetivo de constatar quais dos 4 termos são pares"
    return num
	"Esses números armazenados em num são retornados"