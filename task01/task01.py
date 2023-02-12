#1.Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def degree_digit(digit, degree):

    if degree == 1:
        return digit
    if degree != 1:
        return (digit * degree_digit(digit, degree -1))

    # return a


digit_for_method = int(input("Enter digit: "))
degree_for_method = int(input("Enter degree: "))
print(degree_digit(digit_for_method, degree_for_method))


