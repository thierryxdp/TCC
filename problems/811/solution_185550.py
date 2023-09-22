def colchao(dimensao, h, l):
    '''dimensao é dada como uma lista com as dimensões do colchão ordenadas
    do menor para o maior, onde h e l saó altura e largura das portas; função
    retorna se é possível passar ou não o colchão pela porta;
    list(int, int, int), int, int -> bool'''
    if dimensao[1]<l:
        return True
    if dimensao[1]<h and dimensao[0]<l:
        return True
    if dimensao[2]<h and dimensao[0]<l:
        return True
    if dimensao[1]<l and dimensao[2]<l:
        return True 
    else:
        return False