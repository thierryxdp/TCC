def retira_pontuação(frase):
    """Função que recebe uma frase e retorna a mesma frase sem os caracteres de pontuação
       parâmetro de entraa:str
       parâmetro de saída:str"""
    return str.replace(frase,'-','') and str.replace(frase,',','') and str.replace(frase,':','') and str.replace(frase,';','') and str.replace(frase,'.','')