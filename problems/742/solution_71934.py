def substitui(s,x,i):
    """ funçao que retorna uma string = s, porem o elemento da posiçao i tem que ser substituido por x. E i precisa ser um inteiro entre 0 e o tamanho da string;
    	str, str, int -> str;
    	exemplo1 -> 'oi tudo bem' + 'a' + 6= 'oi tudo bem 6'
        exemplo2 -> 'tchau' + 'o' + 2= 'tchau 2' """
        return str(s[:i]) + x + str(s[i+1:])