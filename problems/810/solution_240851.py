def retira_pontuacao1(frase):
    """Dada uma frase, a função vai substituir todos caracteres
    de pontuação(exclamação, interrogação, reticências, ponto final,
    dois pontos, vírgula, ponto e vírgula ou travessão) por um caractere
    de espaço.
    A frase deve ser escrita entre aspas;
    str --> str"""
    frase = frase.replace("!","/")
    frase = frase.replace("?","/")
    frase = frase.replace("...","/")
    frase = frase.replace(".","/")
    frase = frase.replace(":","/")
    frase = frase.replace(",","/")
    frase = frase.replace(";","/")
    frase = frase.replace("-","/")
    frase = frase.split("/")
    frase = " ".join(frase)
    return frase

def inverte(frase):
    """Dada uma frase como parâmetro, a função retorna uma outra
    frase contendo as mesmas palavras da frase incial em ordem inversa,
    sem letras maiúsculas e sem pontuação. Exemplo: (Nossa, que fome) vai
    retornar (fome que nossa).
    A frase deve ser escrita entre aspas;
    str --> str"""
    frase = retira_pontuacao1(frase)
    frase = str.lower(frase)
    frase = frase.split()
    frase = frase[::-1]
    frase = " ".join(frase)
    return frase