def posLetra(s,l,n):
    """Função que retorna a posição da string mediante a ocorrencia 'n' da letra 'l'
        str,str,int->int"""
    posicao=0
    while posicao < len(s):
        if l in s:
            frase=str.replace(s,l,'/',n-1)
        posicao=posicao+1

    if l in frase:
        return str.find(s,l)