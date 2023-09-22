# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Esse código recebe uma palavra, e substitui a letra 
    que esta na posição 'i' pelo caracter 'x' inserido"""
   
    return s[0:i]+ x + s[i+1: ]