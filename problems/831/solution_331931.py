def lingua_p(palavra):
    '''função que recebe uma palavra e retorna uma nova na Língua do P
    string -> string'''
    novaP = '' 
    for i in palavra:
    	if i in 'aáeéiíoóuú':
            novaP = novaP + i + 'p' + i
        else: 
            novaP = novaP + i
    return novaP