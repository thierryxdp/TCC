# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e insere o caractere # no início, no meio e no final dela.
    string -> string"""
    return str('#')+str(s[0:((len(str(s)))//2)])+'#'+str(s[((len(str(s)))//2):])+str('#')