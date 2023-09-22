def posLetra(frase,letra,numero):
    '''recebe uma string, uma letra, e uma numero para a ocorrencia da letra e retorna a posição
    da string da ocorrencia da letra
    posLetra('foi pelas festas da coroação', 's', 4)
    posLetra('conte-me as festas da coroação', 'e', 1)'''
    repeticao = []
    caracteres = []
    inicio = 0
    
    while len(repeticao) < numero:
        caracteres = caracteres + [letra]

        if letra not in frase:
            ocorrencia = -1
            break
            
        if frase[inicio] == letra:
            repeticao = repeticao + [letra]
            frase = frase.replace(frase[inicio],'.')
        inicio = inicio + 1
        ocorrencia = (len(caracteres) - 1)
        
    return ocorrencia