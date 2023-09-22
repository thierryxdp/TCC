def posLetra(frase,letra,numero):
    '''recebe uma string, uma letra, e uma numero para a ocorrencia da letra e retorna a posição
    da string da ocorrencia da letra'''
    repeticao = []
    caracteres = []
    inicio = 0
    
    while len(repeticao) < numero:
        caracteres = caracteres + [letra] 
        if not letra in frase:
            return -1
        
        if frase[inicio] == letra:
            repeticao = repeticao + [letra]
        inicio = inicio + 1

    return (len(caracteres) - 1)