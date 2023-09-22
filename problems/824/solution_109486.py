def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase,
       mas com as consoantes em letras maiúsculas
       parâmetros de entrada:str
       parâmetro de saída:str"""
    i=0
    frase_tratada=''
    while i<len(frase):
        caractere=frase[i]
        if caractere in 'bcçdfghjklmnpqrstvwxyz ':
            caractere= str.upper(caractere)
        frase_tratada=frase_tratada+caractere
        i=i+1
    return frase_tratada