# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
        """coloque de entrada s uma string, x um caractere e i um número entre 0 e o comprimento da string e retorne a string sendo que o elemento da posição s é substituído pelo caractere"""
        return s[:i]+str(x)+s[i+1:]