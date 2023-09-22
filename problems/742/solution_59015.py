# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    " Função que pega uma string,cacatere e um numero. realiza o fatiamento e utiliza esses dados str, int --> str"
    palavra = s
    letra = x
    numero = i
    soma = numero + 1
    
    
    return palavra[0: numero] + letra + palavra[soma: ]