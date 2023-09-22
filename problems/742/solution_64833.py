# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string igual a 's' exceto
    que o elemento da posição 'i' deve ser substituido 
    pelo caractere 'x' '''
    comprimentoStr= 0<i<len(str(s))
    susbstituindo= s[0:i]
    resto= s[(i+1):]
    return susbstituindo+str(x)+resto