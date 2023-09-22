# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna a string fornecida com a troca de um elemento na posição desejada 
    Parameters:
    s: string
    x: novo caractere
    i: posição do elemento a ser substituído
    
    Returns:
    Uma nova string com o elemento substituído pelo novo caractere"""
    return s[ :i] + x + s[i+1: ]