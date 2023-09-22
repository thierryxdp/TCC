def uppCons(frase:str) -> str:
    """Função torna as consoantes da frase maiusculas

       frase:
       numeros: frase a ser analisada

       Return:
       frase com apenas as consoantes maiusculas
    """
    i = 0
    nova_frase = frase

    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouáàãâéíôu':
           nova_frase = str.replace(nova_frase,nova_frase[i],str.upper(nova_frase[i]))
        i = i + 1
    return nova_frase