# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s, x, i):
    """Funcao que retorna uma s com um elemento substituido
    pelo caractere x, na posição do numero inteiro i.
    Entrada: string, int, int
    Saida: string
    
    parameters:
    stringA: string para ser utilizada
    caractere: caractere para ser colocado
    inteiro: posicao onde o caractere sera alocado
    """
    text = s.replace(s[i], 'x')
    
    return text