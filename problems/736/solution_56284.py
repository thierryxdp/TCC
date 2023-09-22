# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    def abs(x):
    '''função que retorna o valor absoluto de um número;
    int/float --> int/float'''
    if x<0:
        x= -1 * x
    return x

def aniversario(x=1):
    '''.'''
    msg = "Feliz aniversário!! "
    return msg * x

def data(dd, mm, aaaa):
    '''.'''
    if 0 < dia <= 31 and 0 < mes <= 12:
        if 0 < dia < 10 and 0 < mes < 10:
            return "0" + str(dia) + "/0" + str(mes) + "/" + str(ano)
        if 0 < dia < 10:
            return "0" + str(dia) + "/" + str(mes) + "/" + str(ano)
        elif 0 < mes < 10:
            return str(dia) + "/0" + str(mes) + "/" + str(ano)
        return str(dia) + "/" + str(mes) + "/" + str(ano)
    elif dia <= 0 or dia > 31:
        return "O dia informado não existe."
    if mes <= 0 or mes > 12:
        return "O mês informado não existe."

def grafico(y):
    '''.'''
    if y > 6 or y < 0 or y == 0:
        return 0
    else:
        if y <= 2:
            return y
        elif 2 < y <= 3.5:
            return 2
        if 3.5 < y <= 5:
            return 3
        else:
            return y**2 - 10 * y + 28

def inss(b):
    '''.'''
    if b < 0:
        return "O valor " + str(b) + " não é suportado"
    if b <= 2000:
        return 0.06 * b
    elif 2000 < b <= 3000:
        return 0.08 * b
    else:
        return 0.10 * b

def ir(b):
    '''.'''
    if b < 0:
        return "O valor " + str(b) + " não é suportado"
    if b <= 2500:
        return 0.11 * b
    elif 2500 < b <= 5000:
        return 0.15 * b
    else:
        return 0.22 * b

def liquido(b):
    '''.'''
    if b < 0:
        return "O valor " + str(b) + " não é suportado"
    return b - ir(b) - inss(b