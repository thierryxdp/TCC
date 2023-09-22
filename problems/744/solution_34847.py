def hashtag(s):
    """ funçao que retorna uma string com o simbolo # no inicio, meio e fim;
    	str -> str;
        exemplo1 -> 'oi' = '#o#i#';
        exemplo2 -> 'eae' = '#e#ae#' """
    return '#' + str(s[0:len(s)/2]) + '#' + str(s[len(s)/2+1:]) + '#'