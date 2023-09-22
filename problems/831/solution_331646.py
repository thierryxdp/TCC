def lingua_p(string):
    '''retorna a string na lingua do p.
    str->str'''
    string=string.lower()
    v='aeiouáéôõìú'
    for i in range(len(v)):
    	string=string.replace(v[i],v[i]+'p'+v[i])
    return string