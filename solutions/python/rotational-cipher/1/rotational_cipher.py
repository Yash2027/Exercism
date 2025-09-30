def rotate(text, key):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for ch in text:
        found = False

        # check lowercase
        for i in range(26):
            if ch == lowercase[i]:
                new_index = (i + key) % 26
                result += lowercase[new_index]
                found = True
                break

        # check uppercase
        if not found:
            for i in range(26):
                if ch == uppercase[i]:
                    new_index = (i + key) % 26
                    result += uppercase[new_index]
                    found = True
                    break

       
        if not found:
            result += ch

    return result
