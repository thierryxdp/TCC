def lingua_p(palavra):
    '''Recebe uma palavra e retorna uma nova palavra 
    em que é adicionado p mais a vogal original
    str->str'''
    nov_pala=''
    for i in palavra:
        nov_pala=nov_pala+str(i)
        if i in 'aeiuoAEIOUáíúóéÁÉÚÍÓàèùòìÀÈÙÌÒ':
            nov_pala=nov_pala+'p'+str(i)
    return nov_pala