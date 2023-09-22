def conta_frases(s):
    """
"""
    s1 = str.count(s, "...")
    s_depois_das_reticencias = str.replace(s, "...", "XXX")
    s2 = s_depois_das_reticencias
    s3 = str.count(s2, ".")
    s4 = str.count(s2, "!")
    s5 = str.count(s2, "?")
    return s1 + s3 + s4 + s5