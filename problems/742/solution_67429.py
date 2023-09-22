# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funçao que altera uma das letras presentes na string informada pelo utilizador;
    string , int , string= string''' 
    return s[0:i+1] + x + s[i:len(s)]