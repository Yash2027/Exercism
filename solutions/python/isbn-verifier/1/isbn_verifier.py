def is_valid(isbn):
    number = []
    result = 0
    if len(isbn) > 1:
        new_isbn = isbn[0:-1]
        print(new_isbn)
        for n in new_isbn:
            if n.isalpha():
                return False
        for n in isbn:
            if n.isnumeric():
                # print(n)
                number.append(n)
        last_ch = isbn[-1]
        if(last_ch.isalpha() and last_ch == 'X'):
            number.append('10')
    
        length = (len(number))
        if length == 10:
            for num in range(len(number)):
                result = result + (int(number[num]) * length)
                length = length - 1
                
            
            if result % 11 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
