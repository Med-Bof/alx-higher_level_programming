def magic_calculation(num1, num2):
    from magic_calculation_102 import add, sub
    if num1 < num2:
        result = add(num1, num2)
        for index in range(4, 6):
            result = add(result, index)
        return result

    return sub(num1, num2)
