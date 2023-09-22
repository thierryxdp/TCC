def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um número e retorna em que posição da string a letra está; str,str,int -> int'''
    contador = 0 
    ocorrencias = str.count(string,letra)
    if numero>ocorrencias:
        return -1
    else:
        while contador<len(string):
            if string[contador]==letra and str.count(string,letra,contador,contador+1)==1:]
                return contador
        else:
            contador = contador+1
        return contador