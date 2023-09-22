def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário em que cada palavra
    da string é uma chave e seu valor é o número de vezes que a 
    palavra aparece na string.
    assinatura: string --> dict
    testes:
    """
    contador = 0 
    acumulador = {}
    a = str.split(frases)
    while contador < len(str.split(frases)):
        acumulador[a[contador]] = list.count(a,a[contador])
        contador = contador + 1           
    return acumulador