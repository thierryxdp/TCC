def retira_pontuacao(frase):
    
    """Função que, dada uma frase, retorna a frase onde todos os caracteres(incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituidos por espaço. String->String."""
    
    frase1=str.join("#",str.split(frase,"?"))
    frase2=str.join("#",str.split(frase1,"-"))
    frase3=str.join("#",str.split(frase2,","))
    frase4=str.join("#",str.split(frase3,":"))
    frase5=str.join("#",str.split(frase4,";"))
    frase6=str.join("#",str.split(frase5,"."))
    frase7=str.join("#",str.split(frase6,"!"))
    frasedef=frase7.replace("#"," ",-1)
    
    return frasedef