def hashtag(s):
    """ Insere o caractere # no início, no meio e no final da string s.
    	str -> str
        
        Parameter:
        s: String s
        
        Returns:
        A string s com # no início, no meio e no fim.
    """
    return '#' + s[ : len(s) // 2] + '#' + s[len(s) // 2 : ] + '#'