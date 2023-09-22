def classificacao(cv, ce, cs, fv, fe, fs):
    """diz quem é o melhor time
    int,int,int,int,int,int -> string"""
    if pontos (cv,ce)<pontos (fv,fe):
        return 'Flaminthias'
    elif pontos (fv,fe)<pontos(cv,ce):
        return 'Cormengo'
    else:
        if cs>fs:
            return 'Flaminthias'
        elif fs<cs:
            return 'Cormengo'
        else:
            return 'Empate'
        
def pontos (v,e):
    return 3*v+1*e# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):