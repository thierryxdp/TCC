def substitui(s,x,i):
    """ funçao que retorna uma string = s, porem o elemento da posiçao i tem que ser substituido por x. E i precisa ser um inteiro entre 0 e o tamanho da string;
    	str, str, int -> str;
		exemplo1 -> 'ola', 'x', 2= 'olx'
        exemplo2 -> 'beleza?', 'x', 6= 'belezax'"""
        return str(s[:i]) + x