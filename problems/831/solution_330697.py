def lingua_p(palavra):
    """Função que recebe uma palavra em português e retorna esta palavra na
    língua do p, ou seja, após cada vogal da palavra original, é inserida
    a sequência de letras p mais a vogal oriiginal. A palavra retorna toda
    em minúsculas.
    str->str
    """
    linguap = ''
    minus = str.lower(palavra)
    for elemento in minus:
        linguap = linguap + elemento
        if elemento in "AEIOUaeiouÁÉÍÓÚáéíóúÂÊÔâêôãõ":
             linguap = linguap + "p" + elemento
    return linguap