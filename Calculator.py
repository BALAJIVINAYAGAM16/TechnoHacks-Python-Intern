def main():
    num1 = int(input("Enter Number 1:"))
    num2 = int(input("Enter Number 2:"))
    operation = str(input("Enter operation to perform:( + , - , * , /) : "))

    match operation:
        case '+':
            add = num1 + num2
            print(f'Addition of {num1} and {num2} is {add}')
        case '-':
            sub = num1 - num2
            print(f'Subtraction of {num1} and {num2} is {sub}')
        case '*':
            mul = num1 * num2
            print(f'Multiplication of {num1} and {num2} is {mul}')
        case '/':
            div = num1 / num2
            print(f'Division of {num1} and {num2} is {div}')
        case default:
            print("Enter operation given below!!!")
            return main()

    c = str(input("Do you want to continue:(y or n) :"))

    if c == 'y' or c == 'Y':
        return main()
    else:
        return quit()
        
main()
        
