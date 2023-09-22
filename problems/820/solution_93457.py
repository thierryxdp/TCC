def posLetra(string,letra,n):
    """Função que recebe como entradas uma string, uma letra e um número e
    retorna em que posição da string aquela ocorrência está. Havendo menos
    ocorrências do que aquela fornecida, a função deverá retornar -1."""
    """str,str,int-->int"""
    i=0
    ocorrencias=string.count(letra)
    a=''
    if ocorrencias<n:
        return -1
    while i<len(string):
        if string[i]==letra:
            a= a+string[i]
        if string[i]==letra and len(a)==n:
            return i
        i=i+1