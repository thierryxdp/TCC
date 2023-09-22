def posLetra(string, letra, numero):
    """Função que recebe como entrada uma string, uma letra e um numero
    que indica a ocorrencia desejada da letra.
   
    Parameters:
    string: Palavra que será analisada
    letra: Letra que queremos encontrar na string
    numero: numero da ocorrencia da letra
    
    Returns:
    Retorna a posição da string em que aquela ocorrencia da letra 
    aparece
    str, str, int -> int
    """
    i = 0
    lista =[]
    string1 = list(string)
    while i < len(string1) and len(lista)<numero:
        if letra == string1[i]:
            list.append(lista,string1[i])
        i += 1
    return i-1
        else:
        return -1