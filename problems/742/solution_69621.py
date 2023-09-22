# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que pega os valores de entrada s,x e i e retorna uma string modificada 
    	str,str→str'''
    palavra= str(s)
    num= i>= 0 and i <= len(palavra)
    nova= palavra.replace(palavra[i],x)
    return  nova