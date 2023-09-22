def lingua_p(palavra):
    #Fundão que retorna na palavra na lingua P
    #Entrada: Str | Saida: Str 
    vogais = ['a', 'á', 'à', 'ã', 'â', 'e', 'i', 'o', 'u', 'è', 'é', 'í', 'ì', 'ó', 'ò', 'õ', 'ô', 'ú', 'ù', 'û']
    resposta = []
    for letra in palavra:
        if letra in vogais:
            auxilia = letra + "p" + letra 
            list.append(resposta, auxilia)
        else:
            list.append(resposta, letra)
    return str.join("", resposta)