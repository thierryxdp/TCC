# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):   
    """dado a string s, a função retotna o caractere # no início, no meio e no final dela;
    str->str"""
    A=s[:int(len(s)/2)]
    B=s[int(len(s)/2):]
    return'#'+A+'#'+B+'#'