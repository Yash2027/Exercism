def is_isogram(string):
    text = string.lower()
    seen = set()

    for ch in text:
        if ch.isalpha():
            if ch in seen:
                return False
            seen.add(ch)
    return True      
    # pass
