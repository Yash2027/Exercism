def rebase(input_base, digits, output_base):
   
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not digits:
        return [0]

    
    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    result = 0
    length = len(digits) - 1
    for i in range(len(digits)):
        result += digits[i] * (input_base ** length)
        length -= 1

    
    if result == 0:
        return [0]

    converted = []
    while result > 0:
        remainder = result % output_base
        converted = [remainder] + converted
        result = result // output_base

    return converted
