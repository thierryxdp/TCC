# str-> str
def hashtag(string):
    """recebe uma string e insere hashtag no seu inicio,meio e fim"""
    return "#"+ string[0:(len(string)//2)]+"#"+string[(len(string)//2):]+"#"