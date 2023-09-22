def retira_pontuacao(tweet):
    import re
    clean = re.sub(r"""
               [,.;@#?!&$]+  
               \ *           
               """,
               " ",         
               tweet, flags=re.VERBOSE)
    return clean