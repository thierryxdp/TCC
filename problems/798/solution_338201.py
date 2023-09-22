#def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário em que cada palavra
    da string é uma chave e seu valor é o númerp de vezes que a 
    palavra aparece na string.
    assinatura: string --> dict
    testes:
    """
    contador = 0 
    acumulador = {}
    for i in str.count(frases, i, ''):
        if i == str.count(frases, ''):
            contador = contador + 1
            acumulador['i'] = contador            
    return acumulador