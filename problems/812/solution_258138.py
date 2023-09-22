def retira_pontuacao(frase):
    """
    Função que dada uma frase, retone a frase onde todos os 
    caracteres de pontuação(incluindo travessâo, vírgula, dois pontos,
    ponto e vírgula, além da pontuação de encerramento de frase) tenha
    sido substituídos por espaço.
    Paramêtro de Entrada: string
    Valor de Saida: string
    
    """
    
    p= str.split(frase,".")
    excl=str.split(p,"!")
    trav=str.split(excl,"/")
    inter=str.split(inter,"?")
    virg=str.split(inter,",")
    dois_p=str.split(virg,":")
    p_virg=str.split(dois_p,";")
    
    
    return str(p_virg)