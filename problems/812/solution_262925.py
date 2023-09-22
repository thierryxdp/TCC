def substituindo_caracteres_de_pontuação_por_espaço(frase): 
    ''' Essa função recebe uma frase e retorna essa frase substituindo todos os caracteres de pontuação (travessão, vírgula, dois pontos, ponto e
    vírgula, ponto de interrogação, ponto final, ponto de exclamação e reticências) por espaço.
    str-> str.
    '''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(retira_pontuacao(frase),"!"," "),"?"," "),","," "),"."," "),":"," "),";"," "),"-"," ")str.replace(substituição_de_três_pontos_por_um_ponto(frase),"!"," "),"?"," "),","," "),"."," "),":"," "),";"," "),"-"," ")retira_pontuacao