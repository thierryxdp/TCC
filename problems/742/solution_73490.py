# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' casos de teste:
    substitui('banana','t',0)== 'tanana'
    substitui('laranja','m',4)== 'laramja'
                              == 'lara' + 'm' + 'ja'
                              == s[:i-1] + x + s[i+1:]
    '''
    return s[:i-1]+x+s[i+1:]