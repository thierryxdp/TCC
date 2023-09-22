# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Entrada:
    	É fornecido uma string s, um caracter x e um número i ---> str, str, int
    Saída:
    	Substitui o caracter da posição i por x ---> str
    '''
    
    return s[0:i] + str(x) + s[i+1:]