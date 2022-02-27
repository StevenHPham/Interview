def factorial_stack(n):
    stack = []
    # push each call to a stack
    # top of the stack is base case
    while n > 0:
        stack.append(n)
        n -= 1

    res = 1
    # pop and use return value until stack is empty
    while len(stack) != 0:
        res *= stack.pop()

    return res


print(factorial_stack(3))