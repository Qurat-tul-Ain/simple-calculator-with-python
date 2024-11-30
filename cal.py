# A Simple calculator :D

def main():
    val1: int = input("Enter Number: ")
    num1 = int(val1)
    
    op : int = input("Enter op(+,-,*,%,/): ")

    val2 : int = input("Enter Number: ")
    num2  = int (val2)

    result = num1 + num2
   
    print("Calculate value " + str(num1) + " " + op + " " + str(num2) + " = " + str(result))

if __name__ == '__main__':
    main()

