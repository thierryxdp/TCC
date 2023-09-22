def retira_pontuacao(frase):
    """
    Função que dada uma frase, retone a frase onde todos os 
    caracteres de pontuação(incluindo travessâo, vírgula, dois pontos,
    ponto e vírgula, além da pontuação de encerramento de frase) tenha
    sido substituídos por espaço.
    Paramêtro de Entrada: string
    Valor de Saida: string
    
    """
    
    p= str.join(" ",str.split(frase,"."))
    excl=str.join(" ",str.split(p,"!"))
    trav=str.join(" ",str.split(excl,"/"))
    inter=str.join(" ",str.split(inter,"?"))
    virg=str.join("", str.split(inter,","))
    dois_p=str.join(" ",str.split(virg,":"))
    p_virg=str.join(" ",str.split(dois_p,";"))
    
    
    return str(p_virg)