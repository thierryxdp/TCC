# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que retorna,a partir de uma string s, uma nova string com o elemento da poisição i substituido pelo caractere x; string,string,int->string'''
    letrai=s[i]
    return str.replace(s,letrai,i)