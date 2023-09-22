# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     ''' funcao que recebe uma string, um caracter e o numero do lun da string
        entra:
        string, caracter, int
        sai:
        string
    '''
    
   return  s[0:i] + x + s[i+1:]