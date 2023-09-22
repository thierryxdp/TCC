# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui letra em posição escolhida.
       str--> str'''
parteum = s[0:i]
partedois = s[i+1:len(s)]
return parteum + x + partedois