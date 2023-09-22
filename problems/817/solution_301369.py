def acima_da_media(ls):
    """
"""
    media = (sum(ls))/len(ls)
    list.sort(ls)
    return ls[list.index(ls,media):]