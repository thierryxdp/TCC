# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     """Recebe string (s), um caractere (x) e um número 
     inteiro (i) maior que 0 e menor que o comprimento 
     da string, retorna uma nova string "substituindo" o
     caracter da posição informada pelo novo caracter;
     str, str, int -> str"""
        if i<len(s) and i<=0:
            return s[:i] + x + s[i+1:]