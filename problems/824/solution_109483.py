def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase,
       mas com as consoantes em letras maiúsculas
       parâmetros de entrada:str
       parâmetro de saída:str"""
    i=0
    frase-tratada=''
    while i<len(frase):
        caractere=frase[i]
        if caractere in 'bcdfghjklmnpqrstwyz ':
            caractere= str.upper(caractere)
        frase-tratada=frase-tratada+caractere
        i=i+1
    return frase-tratada