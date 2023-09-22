def inverte(frase):
    ''' Função que dada uma string (frase) que represente uma frase,
    retorna uma outra frase com as mesmas palavras na ordem inversa,
    sem as maiúsculas e sem a pontuação.
    Entrada: str
    Retorno: str '''

    sem_caracteres = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"...","."),"."," "),"?"," "),"!"," "),"-"," "),","," "),":"," "),";"," ")
    sem_maiuscula = str.lower(sem_caracteres)
    lista_semespaco = str.split(sem_maiuscula)
    palavras_invertidas = lista_semespaco[::-1]
    frase_final = str.join(" ",palavras_invertidas)

    return frase_final