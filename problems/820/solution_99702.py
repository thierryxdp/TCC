def posLetra(string,letra,n):
    """Função que recebe como entrada uma (string), uma (letra) e um (numero)
    e retorna a posição do (numero) de ocorrencia da letra dentro da string.
    string, string, int -> int"""

    lst=[]
    i=0
    vazio=''
    if n <= string.count(letra):
        while i<len(frase):
            if string[i] in letra:        
                list.append(lst,i)
            i=i+1
        return lst[n-1]
    else:
        return -1