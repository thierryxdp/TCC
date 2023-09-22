# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(string,x,i):
    """ essa função retornará uma string dada como parâmetro, porém com seu caracter ocupante da posição 1 substituido pelo x
    string,int,int->string
    """
    if 0<i<len(string):
        return string[:i]+x+string[i+2:]
    else:
        return "o parâmetro de entrada i é um número maior que a string"