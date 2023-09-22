# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    Funcao que retorna uma string igual a s, exceto que o elemento
    da posicao i deve ser substituido pelo caractere x.
    Parametro de Entrada: string,string,int
    Valor de Saida: string
    """
    return s.replace(s[i:i+1],x)