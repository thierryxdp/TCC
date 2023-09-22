def lingua_p(p):
    '''Função que recebe uma palavra em português e retorna a mesma traduzida para a língua do p
       str->str'''
    j=1
    lista=[]
    for var in p:
        lista.append(var)
        if var=="a" or var=="e" or var=="o" or var=="u":
            lista.insert(j, "p"+var)
            j=j+2
        j=j+1
    return str.join("",lista)