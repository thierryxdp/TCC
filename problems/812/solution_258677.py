def retira_pontuacao(string):
    """Função que dada uma frase troque todos os caracteres de pontuação por espaços. string -> string"""
    str1 = str.replace(string,"-"," ")
    str2 = str.replace(str1,","," ")
    str3 = str.replace(str2,":"," ")
    str4 = str.replace(str3,";"," ")
    str5 = str.replace(str4,"."," ")
    return str5