def retira_pontuacao(frase):
    """dada uma frase, a função retorna essa mesma frase sem os caracteres de pontuação (travessão, vírgula, dois 
    pontos e ponto e vírgula, além da pontuação de encerramento da frase), isto é, substituindo-os por espaço; 
    string -> string"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"-"," "),","," "),":"," "),";"," "),"..."," "),"."," "),"?"," "),"!"," ")