def posLetra (string,letra,n):
    """Função que retorna a letra pedida input str, str, int, return int or str"""
    index=0
    contador=0
    soma=0
    while contador <= n:
        soma = soma + index
        index= str.find(string,letra,soma)
        contador = contador + 1 
        return -1