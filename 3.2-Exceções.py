def divisao42(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print('Não é possível dividir por zero')

print(divisao42(2))
print(divisao42(12))
print(divisao42(0))
print(divisao42(5))