# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Funcao que recebe uma string, um caractere e um
    inteiro e substitui a posicao do numero inteiro 
    na string pelo caractere recebido
    
    string, int, int -> string
    '''
    if i==0:
        return x + s[1:]

	if i==len(s):
        return s[:len(s)] + x


	if i>0:
        return s[:i] + x + s[i+1:]