# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e insere o caractere "#" no início,
       meio e no final dela.
       
       Parameters:
       s: String escolhida
       """
    return '#' + s[0:len(s)//2] + '#' + [len(s)//2:] + '#'