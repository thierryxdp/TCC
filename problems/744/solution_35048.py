def hashtag(s):
    """função que coloca "#" no início, no meio e no final da str dada. str->str"""
    i=len(s)/2
    mensagem='#'+s[0:i]+'#'+s[i: ]+"#"