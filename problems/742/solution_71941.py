def substitui(s,x,i):
    """ funçao que retorna a string s, porem o termo de posiçao i deve ser subsituido pelo caractere x;
    	str, str, int -> str;
    	exemplo1 -> 'oi', 'x', 0= 'xi';
        exemplo2 -> 'eae', 'x', 1= 'exe' """
    return str(s[0:i]) + str(x) + str(s[i+1:})