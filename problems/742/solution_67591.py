# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    11 >= i >= 0
    if i == 0:
        s = str(x) + s[1:11]
        return s[0:11:1]
    elif i == 1:
        s = s[0:1] + str(x) + s[2:11]
        return s[0:11:1]
    elif i == 2:
        s = s[0:2] + str(x) + s[3:11]
        return s[0:11:1]
    elif i == 3:
        s = s[0:3] + str(x) + s[4:11]
        return s[0:11:1]
    elif i == 4:
        s = s[0:4] + str(x) + s[5:11]
        return s[0:11:1]
    elif i == 5:
        s = s[0:5] + str(x) + s[6:11]
        return s[0:11:1]
    elif i == 6:
        s = s[0:6] + str(x) + s[7:11]
        return s[0:11:1]
    elif i == 7:
        s = s[0:7] + str(x) + s[8:11]
        return s[0:11:1]
    elif i == 8:
        s = s[0:8] + str(x) + s[9:11]
        return s[0:11:1]