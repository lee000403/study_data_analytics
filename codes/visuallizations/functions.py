# package == module(python)

# 기본 function 구성
def function_name() :
    pass
    return 0

function_name()
pass

# 평범한 params 이용한 결과값 받기
def add(first, second):
    sum = first + second
    return sum

result_sum = add(4, 6)
pass

def minus(first, second=0):
    result = first - second
    return result

result_minus = minus(2, 4)
minus(3)

# return tuple datatype
def multiply(first, second=1):
    multiply = first * second
    # like list [multiply, first, second]
    return (multiply, first, second)

result_multiply = multiply(3, 4)
# (multiply, first, second) = multiply(4)
_result, first, second = multiply(4)
# result, result_first, result_second = multiply(4)
pass