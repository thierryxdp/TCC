# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna uma string com "#" no início, no meio e no
       fim dessa string.
       str -> str"""
    quant=len(s)
    meiopar=quant/2
    meioimp=(quant+1)/2
    if quant%2==0:
        return "#"+s[0:int(meiopar)]+"#"+s[int(meiopar):quant]+"#"
    else:
        return "#"+s[0:int(meioimp)-1]+"#"+s[int(meioimp):quant]+"#"