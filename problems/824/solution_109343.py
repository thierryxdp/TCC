def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase,
       mas com as consoantes em letras maiúsculas
       parâmetros de entrada:str
       parâmetro de saída:str"""
    i=0
    consoante=''
    while i<len(frase):
        consoante=consoante+frase[i]
        frase=str.upper(consoante)
    return frase