# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) == 0:
     return str() + '###'
    elif len(s) == 1:
     return str() + '##' + s + str() + '#'
    elif len(s) == 2:
     return str() + '#' + s[0:1] + str() + '#' + s[1:2] + str() + '#'
    elif len(s) == 3:
     return str() + '#' + s[0:1] + str() + '#' + s[1:3] + str() + '#'
    elif len(s) == 4:
     return str() + '#' + s[0:2] + str() + '#' + s[2:4] + str() + '#'
    elif len(s) == 5:
     return str() + '#' + s[0:2] + str() + '#' + s[2:5] + str() + '#'
    elif len(s) == 6:
     return str() + '#' + s[0:3] + str() + '#' + s[3:6] + str() + '#'
    elif len(s) == 7:
     return str() + '#' + s[0:3] + str() + '#' + s[3:7] + str() + '#'
    elif len(s) == 8:
     return str() + '#' + s[0:4] + str() + '#' + s[4:8] + str() + '#'
    elif len(s) == 9:
     return str() + '#' + s[0:4] + str() + '#' + s[4:9] + str() + '#'
    elif len(s) == 10:
     return str() + '#' + s[0:5] + str() + '#' + s[5:10] + str() + '#'
    elif len(s) == 11:
     return str() + '#' + s[0:5] + str() + '#' + s[5:11] + str() + '#'
    elif len(s) == 12:
     return str() + '#' + s[0:6] + str() + '#' + s[6:12] + str() + '#'    
    elif len(s) == 13:
     return str() + '#' + s[0:6] + str() + '#' + s[6:13] + str() + '#'    
    elif len(s) == 14:
     return str() + '#' + s[0:7] + str() + '#' + s[7:14] + str() + '#'
    elif len(s) == 15:
     return str() + '#' + s[0:7] + str() + '#' + s[7:15] + str() + '#'
    elif len(s) == 16:
     return str() + '#' + s[0:8] + str() + '#' + s[8:16] + str() + '#'
    elif len(s) == 17:
     return str() + '#' + s[0:8] + str() + '#' + s[8:17] + str() + '#'  
    elif len(s) == 18:
     return str() + '#' + s[0:9] + str() + '#' + s[9:18] + str() + '#'