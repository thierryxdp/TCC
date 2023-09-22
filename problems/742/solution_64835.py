# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string igual a 's' exceto
    que o elemento da posição 'i' deve ser substituido 
    pelo caractere 'x' '''
    comprimento=0<i<len(str(s))
    substituicao=s[0:i]
    restante=s[(i+1):]
    return susbstituicao+str(x)+restante