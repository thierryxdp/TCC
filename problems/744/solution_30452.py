# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Função que recebe uma string s e insere o caractere "#" no início,
    no meio e no final da string. Em caso de strings com tamanho ímpar,
    a caractere "#" aparece a esquerda da caractere do meio da string s
    Ex: "abcde" retorna #ab#cde#
    str -> str
    """
    import math
    p="#"+s[:math.floor(len(s)/2)]+"#"+s[math.floor(len(s)/(2)):]+"#"
    return p