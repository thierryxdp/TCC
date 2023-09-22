def colchao(col,h,l):
    '''recebe as dimensoes do colchão e da porta e avalia
    se o colchao passa pela porta
    list+int+int->bool'''
    if col[1] <= h or col[1] <= l:
        return true
    elif col[2] <= h or col[2] <= l:
        return true
    else:
        return false