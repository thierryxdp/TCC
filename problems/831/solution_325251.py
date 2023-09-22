def lingua_p(palavra):
    """receba como parâmetro uma palavrae retorna
esta mesma palavra traduzida para a língua do P,
uma palavra foi traduzida para a língua do P quando,
após cada vogal da palavra original, é inserida a
sequência de letras p mais a vogal original"""
    i = 0
    inteira = ''
    while i < len(palavra):
        if palavra[i] in 'AÃÂEÉÊIÍÎÓOÕUÚaeiouáãâéêíîóõuú': #verifica todas vogais
            inteira +=palavra[i]+ 'p'+palavra[i] #adiciona a vogal atual e a letra p
            i += 1

        else:
            inteira += palavra[i] #apenas adiciona a letra
            i += 1

    return inteira