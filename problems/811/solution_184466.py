def colchao([a,b,c],h,l):
    '''funçao que tendo como entrada uma listaas três dimensões de um 
    colchão em formato de paralelepidedo reto(a,b,c) e a altura h e a 
    largura l de uma porta retorna se o colchão passa pela porta.
    list, int, int -> bool'''
    if l>a and h>b:
        return True
    if l>a and h>c:
        return True
    else:
        False