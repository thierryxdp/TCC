def hashtag(s):
    """funçao que recebe uma string s e insere o caractere '#' no inicio, meio e final;
    entrada: str;
    saida: str."""
    inicio = s [0: (len (s) // 2)] 
    meio = s [(len (s) // 2):] 
    return  '#' + str (inicio) + '#' + str (meio)  + '#'