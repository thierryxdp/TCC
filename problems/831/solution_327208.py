def lingua_p(palavra):
    """Função que dada uma palavra em português, retorna essa mesma palavra
       traduzida para a língua do P. Uma palavra foi traduzida para a 
       língua do P quando, após cada vogal da palavra original, é inserida 
       a sequência de letras 'p' mais a vogal original. Ignorando a 
       diferença entre maúsculas e minúsculas.
       str -> str
       
       Parâmetros:
       palavra: palavra em Português que será traduzida para a língua do P
       
       Returns: A palavra traduzida seguindo o padrão descrito no enunciado
                e toda em minúscula.
    """
    str.lower(palavra)
    contador = 0 
    while contador < len(palavra):
        if palavra[contador] in "aeiou":
            palavra = palavra[:contador+1] + 'p' + palavra[contador:]
            contador += 2
        contador += 1
    return palavra