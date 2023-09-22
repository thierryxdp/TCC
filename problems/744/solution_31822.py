# A função inserirá um hashtag no inicio, no meio e no final da string inputada.
# str-> str
def hashtag(s):
    string="#"+s+"#"
    meio=len(string)//2
    string=string[:meio]+"#"+string[meio:]
    return(string)
hashtag