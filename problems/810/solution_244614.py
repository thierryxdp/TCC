def retira_pontuacao(frase):
    "Função que recebe uma frase, e retornaremos ela sem nenhum caracter de pontuação, apenas com espaços onde eram esses caracters. str -> str"
    
    novo1 = frase.replace("-", " ")
    novo2 = novo1.replace(",", " ")
    novo3 = novo2.replace(":", " ")
    novo4 = novo3.replace(";", " ")
    novo5 = novo4.replace(".", " ")
    novo6 = novo5.replace("?", " ")
    novo7 = novo6.replace("!", " ")
    novo8 = novo7.replace("...", " ")

def inverte(frase):
    
    nova_frase = frase(novo8).lower()    
    
    return nova_frase