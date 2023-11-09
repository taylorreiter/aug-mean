def mean(num_list):
    if any(isinstance(num, complex) for num in num_list):
       return NotImplemented 
    else: 
        try:
            return sum(num_list)/len(num_list)
        except ZeroDivisionError :
            return 0
        except TypeError as detail :
            msg = "The algebraic mean of an non-numerical list is undefined.\
                   Please provide a list of numbers."
            raise TypeError(detail.__str__() + "\n" +  msg)
