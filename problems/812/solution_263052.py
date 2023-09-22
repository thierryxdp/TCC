def retira_pontuacao(frase):
    """Recebe uma frase, substitui caracteres de pontuacao substituidos por espaco e retorna a frase; str-> str."""
    frase1=str.split(frase,"!")
    frase2=str.split(frase1,".")
    frase3=str.split(frase2,"?")
    frase4=str.split(frase3,",")
    frase5=str.split(frase4,";")
    frase6=str.split(frase5,":")
    frase7=str.spli(frase6,"-")
    frase_final=srt.join(" ",frase7)
    return str(frase7)