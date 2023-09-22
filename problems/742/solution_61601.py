# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dados uma string s, um caractere x e um número i entre 0 e o 
        comprimento da string, retorna uma string igual a s, exceto que o 
        elemento da posição i deve ser substituído pelo caractere x
        str,str,int->str'''
    ultimo_caracter=len(s)-1
    proximo_caracter=i+1
    
    if i==0:
        return x+s[1:]
    elif 0<i<ultimo_caracter:
        return [0:i]+x+[(i+1):]
    elif i==ultimo_caracter:
        return [0:ultimo_caracter]+x