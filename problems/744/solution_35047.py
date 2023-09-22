def hashtag(s):
    """função que coloca "#" no início, no meio e no final da str dada. str->str"""
    mensagem='#'+s[0:(len(s)/2)]+'#'+s[(len(s)/2): ]+"#"