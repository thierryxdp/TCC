def lingua_p(string):
    '''função que recebe uma palavra e retorna a mesma na língua do p
    str->str'''
    palavra=str.lower(string)
    traducao=[]
    for i in palavra:
        if i in 'aeiouáàãâéèêíìîóòõôùúû':
            traducao.append(i+'p'+i)
        else:
            traducao.append(i)
    return ''.join(traducao)