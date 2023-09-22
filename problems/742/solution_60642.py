# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que retorna uma string com  um novo caractere,
    dados de entrada a string original, o novo caractere 
    substituto e a posição desse novo caractere
    entrada: str,str,int
    saída: str"""
    sub_s=s[0:i]+x+s[(i+1):-1]
    return sub_s