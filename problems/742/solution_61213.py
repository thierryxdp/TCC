# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string igual a s e substitui o número inteiro i por 
    	um caracter x.
        str, str, int -> str'''
    
    retorno = s[0:i]+x+s[-(len(s)-(i+1)):]
    
        return retorno