def inverte(texto):

    """
        Função que recebe um texto e inverte a ordem. A função deixar as letras minusculas e retira todos as pontuações.
        (1) A variável frase_final vai ser a entrada (texto) sem pontuação
        (2) A variável texto_final vai ser a fras_final invertida, para isso utilizamos o método split() e slicer[::-1]

        str --> str
        
    """

    
    frase_final  = ""
    texto_final = ""
    if texto in ["", " "]:
        return texto_final
    else:
        sinal = 0
        for i in range(len(texto)-1):
            if texto[i] ==  " ":
                pass
            if sinal == 0:
                if texto[i] == ".":
                    if texto[i+2] == ".":
                        sinal = 2
                        frase_final+= " "
            if sinal != 0:
                sinal -= 1
            else:
                if texto[i] not in [".",",","!","?",":",";"]:
                    frase_final += texto[i].lower()
                else:
                    frase_final += " "
        for j in frase_final.split()[::-1]:
            texto_final+=j +" "
    return texto_final