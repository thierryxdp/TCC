def findnth(haystack, needle, n):
    parts= haystack.split(needle, n)
    if len(parts)<=n:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)