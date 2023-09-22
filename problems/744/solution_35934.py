def hashtag(s):
    """Coloca hasgtags no início, meio e fim da string
    str -> str"""
    return f"#{s[0:len(s)//2]}#{s[-1:len(s)//2]}#"