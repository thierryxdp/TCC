def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase,
       mas com as consoantes em letras maiúsculas
       parâmetros de entrada:str
       parâmetro de saída:str"""
    i=0
    consoante=''
    while i<len[frase]:
        if frase[i] in 'AEIOUaeiou':
            consoante=str.upper(frase)
    return consoante