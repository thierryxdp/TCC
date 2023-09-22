# str-> str
def hashtag(s):
    """Função recebe uma str e insere o caractere ”#” no inıcio, 
    meio efinal; str-> str"""
    s = "#" + s[ :len(s) // 2]
    return s