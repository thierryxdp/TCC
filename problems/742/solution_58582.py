# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que retorna a substituicao de um caractere na string indicada, retirando o caractere antigo da posicao i e substituindo pelo caracter x, sendo s uma string, x a letra que substituira a posicao i e i o indice'''
    numero= int(i)
    carac1= s[0:i]
    carac2= s[i+1:]
    funcao= carac1+str(x)+carac2
    return funcao