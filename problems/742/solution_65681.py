# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
        Recebe uma string s, faz uma cópia e substitui o elemento
        de posição de posição i em s pelo caracter x
        str, str , int -> str
    '''
    
    if i <= len(s):
        p1 = s[i]
        p2 = p1 = x
        return s[:i] + p2 + s[i+1:]
    else:
        return 'Index maior que o tamanho da string'