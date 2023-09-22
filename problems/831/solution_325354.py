def lingua_p(p):
    '''Função que recebe uma palavra em português e retorna a mesma traduzida para a língua do p
       str->str'''
    j=1
    lista=[]
    for var in p:
        lista.append(var)
        if var=="a" or var=="e" or var=="i" or var=="o" or var=="u" or var=="á" or var=="é" or var=="í" or var=="ó" or var=="ú":
            lista.insert(j, "p"+var)
            j=j+2
        j=j+1
    return str.join("",lista)