def retira_pontuacao(frase):
    """
    Função que dada uma frase, retone a frase onde todos os 
    caracteres de pontuação(incluindo travessâo, vírgula, dois pontos,
    ponto e vírgula, além da pontuação de encerramento de frase) tenha
    sido substituídos por espaço.
    Paramêtro de Entrada: string
    Valor de Saida: string
    
    """
    
    retira = str.strip(frase, "-")
    #/.;:?!
    retira1=str.replace(retira,   "!"," ")
    retira2=str.replace(retira1,  "?"," ")
    retira3=str.replace(retira2,  "."," ")
    retira4=str.replace(retira3,  "/"," ")
    retira5=str.replace(retira4,  ":"," ")
    retira6=str.replace(retira5,  ";"," ")
    retira7=str.replace(retira6,  "-"," ")
    retira8=str.replace(retira7,  ","," ")
    return retira8