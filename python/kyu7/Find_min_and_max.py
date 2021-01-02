def get_min_max(seq): 
    seq.sort()
    tuple = (seq[0], seq[-1])
    return tuple
