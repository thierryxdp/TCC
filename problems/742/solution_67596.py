# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    16 >= i >= 0
    if i == 0:
        s = str(x) + s[1:16]
        return s[0:16:1]
    elif i == 1:
        s = s[0:1] + str(x) + s[2:16]
        return s[0:16:1]
    elif i == 2:
        s = s[0:2] + str(x) + s[3:16]
        return s[0:16:1]
    elif i == 3:
        s = s[0:3] + str(x) + s[4:16]
        return s[0:16:1]
    elif i == 4:
        s = s[0:4] + str(x) + s[5:16]
        return s[0:16:1]
    elif i == 5:
        s = s[0:5] + str(x) + s[6:16]
        return s[0:16:1]
    elif i == 6:
        s = s[0:6] + str(x) + s[7:16]
        return s[0:16:1]
    elif i == 7:
        s = s[0:7] + str(x) + s[8:16]
        return s[0:16:1]
    elif i == 8:
        s = s[0:8] + str(x) + s[9:16]
        return s[0:16:1]
    elif i == 9:
        s = s[0:9] + str(x) + s[10:16]
        return s[0:16:1]
    elif i == 10:
        s = s[0:10] + str(x) + s[11:16]
        return s[0:16:1]
    elif i == 11:
        s = s[0:11] + str(x) + s[12:16]
        return s[0:16:1]