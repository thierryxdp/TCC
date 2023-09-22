def hashtag(s):
    '''Função que retorna uma string s, porém com o caractere "#" em seu início, meio e fim;
    entrada: str;
    saída:str;
    '''
    s1 = '#' + s[:(len(s)//2)] + '#' + s[len(s)//2:] + '#' #variável igual à string de entrada após a operação de concatenação dos caracteres "#";
    return s1