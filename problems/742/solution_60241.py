# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe  uma string 's', um caractere 'x' e um número inteiro 'i' entre 0 
       e o comprimento da string. Retorna uma string com o elemento da posição 'i'
       substituído pelo caractere 'x'
       Parâmetros de entrada:str,str,int
       Parâmetros de saída:str"""
    
    return s[0:i]+x+s[i:]