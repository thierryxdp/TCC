# str-> str

def hashtag(x):
    meio=(len(x))//2
    return "#"+x[0:meio]+"#"+x[meio:len(x)]+"#"