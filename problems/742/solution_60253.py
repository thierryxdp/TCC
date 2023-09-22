# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string "s", um caractere "x" e um número inteiro "i"
       entre 0 e o comprimento da sting e retorna uma srting igual a "s", exceto que 
       o elemento da posição i será substituído pelo caractere "x"
       str,int,int->str
       
       Parâmetros:
       s:a string que será modificada.
       x:O caractere que irá substituir o anterior da string.
       i:O número que representa qual posição deve ser substituída na string.
       
       returns: uma string igual a "s", exceto pelo elemento da posição i que será
                substituído pelo caractere "x"
    """
    return s[0:i]+x+s[i:len(s)]