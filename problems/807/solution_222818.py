def conta_frases(textofrase):
    ''' funcao que recebe um texto e retorna
        o numero de frases que ha no texto.
        as frases terminam com: '.', '...', '!' ou '?',
        pontos de exclamacao e interrogacao nao aparecerao
        repetidamente em sequencia
        str->int'''
    if '...' in textofrase:
        return str.count(textofrase,'.')+ str.count(textofrase,(str.replace(textofrase,'...','?')))+str.count(textofrase,'!')