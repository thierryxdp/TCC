def hashtag (s):
    """."""

    x = len(s)

    return "#"+s[:x//2]+"#"+s[x//2:]+"#"