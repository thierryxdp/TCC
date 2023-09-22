def retira_pontuacao(texto):
    """
        Função que recebe um texto em formato de string e retorna esse mesmo texto retirando a pontuação e colocando um espaço no lugar.
        (1) Os pontos que vão ser trocados por ' ' são ., virgula(,), !,?,:,; e ...
        (2) A variável sinal verifica se estamos analisando a pontuação de ..
        (3) A nova frase, que vai ser retornada pela função, fica armazenada na variável frase_final

        str --> str
        
    """
    frase_final = ""
    if texto in [" ", "  " ]:
        return frase_final
    else:
        sinal = 0
        for i in range(len(texto)-1):
            if sinal == 0:1
                if texto[i] == " . ":
                    if texto[i+2] == " . " :
                        sinal = 2
                        frase_final+= "" 
            if sinal != 0:
                sinal -= 1
            else:
                if texto[i] not in [".",",","!","?",":"," ; "] :
                    frase_final += texto[i]
                else:
                    frase_final += " "  "
    return frase_final