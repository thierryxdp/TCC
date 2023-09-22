def conta_frases(texto):
    """
        Função que recebe um texto no formato de string e retorna o número de frases contida nesse texto
        
        (1)Essa função reconhece as seguintes pontuações .,?,! e ...
        (2)Caso as pontuações de ?,!,. e ... sejam repetidas o resultado não vai ser o correto.
        (3)Caso nao seja inserido nenhuma fras essa função vai retornar 0.
        (3)A variável sinal é utilida para verificar quando o programa não esta analisando a pontuação ...

        str --> int
        
    """
    contadora = 0
    if texto == ' ':
        return contadora
    else:
        sinal = 0
        for i in range(len(texto)):
            if sinal == 0:
                if texto[i] == '.':
                    if texto[i+2] == '.':
                        contadora += 1
                        sinal = 2
            if sinal != 0:
                sinal -= 1
            else:
                if texto[i] in ["!",".","?"]:
                    contadora += 1
    return contadora