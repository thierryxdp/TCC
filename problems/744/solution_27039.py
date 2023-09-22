# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Função que recebe uma string e insere o caractere "#" no início, meio e final dela.
    str-> str
    
    Parameters:
    s: Parâmetro do tipo str que representa a string desejada
    
    """
    s='#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'
    return s