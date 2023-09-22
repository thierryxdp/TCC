# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna a string com # no inicio, no meio e no final;
    str -> str"""
    meio_par=len(s)/2
    meio_impar=len(s)//2
    if len(s)%2==0:
        return'#'+s[0:meio_par+1]+'#'+s[meio_par:]+'#'
    else:
        return'#'+s[0:meio+impar+1]+'#'+s[meio_impar:]+'#'