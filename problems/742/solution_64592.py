# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Recebe uma string s, e substitui o caracter da posição i pelo x que foi dado'''
    retorno = s[:i] + str(x)
    retorno += s[i+1:]
    
    return retorno