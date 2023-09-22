def retira_pontuacao(frase):
    """Retorna uma frase semelhante a original dada como entrada, porém com
    todos os caracteres de pontuação substituídos por espaço.
str -> str"""
    frase1 = str.replace(frase,"—"," ")
    frase2 = str.replace(frase1,","," ")
    frase3 = str.replace(frase2,":"," ")
    frase4 = str.replace(frase3,";"," ")
    frase5 = str.replace(frase4,"."," ")
    frase6 = str.replace(frase5,"!"," ")
    frase7 = str.replace(frase6,"?"," ")
    return frase7

#Casos de teste:
# retira_pontuacao("oi,tudo bem? eu to bem tambem.") == 'oi tudo bem  eu to bem tambem '
# retira_pontuacao("ele disse: — olá!") == 'ele disse    olá '
# retira_pontuacao("meu nome é Beatriz, mas pode me chamar de Bia") == 'meu nome é Beatriz  mas pode me chamar de Bia'