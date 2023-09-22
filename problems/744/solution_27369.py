def hashtag(s):
    """funçao que recebe com s uma string e insere o caractere '#' no inicio, meio e final;
    entrada: str;
    saida: str."""
     
    return  '#' + s [0: (len (s) // 2)]  + '#' + s [(len (s) // 2):]  + '#'