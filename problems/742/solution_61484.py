# substitui em uma posição da string um carctere por outro ex: maça->moça
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que substitui dentro de uma str em uma posição espécifica um caractere 
    	por outro'''
    tam_s=len(s)
    if 0<=i<=(tam_s - 1):
        return s[:i] + x + s[i+1:]
    else: 
        return 'i nã pode ser maior do que o tamanho da string'