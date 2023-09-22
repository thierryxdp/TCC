# receba uma string e insira o caractere ”#” no início, no meio e no final dela
# string e '#'.
# str-> str
def hashtag(s): 
    return '#'+s[:int((len(s))/2)]+'#'+s[int((len(s))/2):]+''