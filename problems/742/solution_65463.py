# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i]+x+s[i+1:]

#Casos de teste
#substitui('IRAJA','j',4) == 'IRAJj'
#substitui('livia','V',2) == 'liVia'
#substitui('palacio','P',0) == 'Palacio'