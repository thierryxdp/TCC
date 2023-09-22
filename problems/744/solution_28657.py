# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    """Dada uma string 's', retorna essa string com o caractere '#' no 
    início, no meio e no final dela.
    str -> str"""
    
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'