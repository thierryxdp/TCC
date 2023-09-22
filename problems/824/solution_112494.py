def uppCons(frase):
    """ Função que recebe como entrada uma frase e retorna
        a frase com todas as suas consoantes em maiúsculas
        (e os demais caracteres exatamente como estavam na 
        frase original);
        string -> string """
    i = 0 #representa os índices da string frase 
    while i<len(frase):
        if str.lower(frase[i]) in 'bcdfghjklmnpqrstvwxyzç':
            frase = str.replace(frase,frase[i],str.upper(frase[i]))
        i = i+1
    return frase