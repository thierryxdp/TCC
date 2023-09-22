#---------------------EXERCICIO 2---------------------

def substitui (s,x,i):
    '''substitui o caractere na posicao i pelo x
       str,str,int ->str'''
    sfatiado1=s[:i]
    sfatiado2=s[(i+1):]
    snovo=sfatiado1+x+sfatiado2
    return snovo