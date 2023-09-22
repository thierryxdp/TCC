def substitui(string,x,i):
    '''str, str, int -> string'''
    '''esta função retorna uma string s, exceto o elemento da posição i, que é substituído por 'x' '''
    'string'[i] = x
	return string[0:i] + x + string[i + 1:]