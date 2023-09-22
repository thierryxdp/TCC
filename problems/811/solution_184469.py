def colchao(medidas,h,l):
    '''funçao que tendo como entrada uma lista com as três dimensões de um 
    colchão em formato de paralelepidedo reto[a,b,c] e a altura h e a 
    largura l de uma porta retorna se o colchão passa pela porta.
    list, int, int -> bool'''
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    if l>=a and h>=b:
        return True
    if l>=a and h>=c:
        return True
    else:
        False