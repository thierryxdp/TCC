def posLetra(string,letra,numero):
    '''Função que recebe uma string, uma letra e um número e retorna em que posição da string a letra está; str,str,int -> int'''
    contador = 0 
    while contador<len(string):
        if string[contador]==letra:
            if str.index(string,letra,numero,len(string)-1)=contador:
                return contador
            else:
                contador = contador+1
        else:
            return -1