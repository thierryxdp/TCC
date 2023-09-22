def lingua_p(string):
    '''funcao que recebe uma string e retorna ela traduzida na lingua do p str->str'''
    palavra=str.lower(string)
    traducao=[]
    for i in palavra:
        if i in 'aeiouáàãâéèêíìîóòõôùúû':
            traducao.append(i+'p'+i)
        else:
            traducao.append(i)
    return ''.join(traducao)