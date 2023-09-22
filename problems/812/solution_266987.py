def retira_pontuacao(frase):
    '''função que retorna todos caracteres de uma frase substituí
    dos por espaços
    entrada: string
    saída: string'''
    virgula=str.count(frase,",")
    travessao=str.count(frase,"/")
    Dois_p=str.count(frase,":")
    ponto=str.count(frase,".")
    inter=str.count(frase,"?")
    excla=str.count(frase,"!")
    ponto_virgula=str.count(frase,";")
    apos=str.count(frase,'-')
    if "," in frase:
        nome= frase.replace(',',' ',virgula)
    if "/" in frase:
        nome= frase.replace('/',' ',travessao)
    if ":" in frase:
        nome= frase.replace(':',' ',Dois_p)
    if "." in frase:
        nome= frase.replace('.',' ',ponto)
    if "?" in frase:
        nome= frase.replace('?',' ',inter)
    if "!" in frase:
        nome= frase.replace('!',' ',excla)
    if ";" in frase:
        nome= frase.replace(';',' ',ponto_virgula)
    if "-" in frase:
        nome= frase.replace('-',' ',apos)
  
    return nome