# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Função que substitui uma caractere de uma string numa posição especificada pela entrada
    	Paramêtros:
        	s: Str -> string
            x: Str -> caractere que substuirá
            i: Int -> posição do caractere a ser substituído, entre 0 e o comprimento da string
        Saída:
        	Str
    '''
    return s[:i] + x + s[i+1:]