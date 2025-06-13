from collections import deque
history=deque(maxlen=8)

def calc(num1,num2,c):
    
    match(c):
        case 1:
            result=num1+num2
            print(f"Result:{result}")
            history.append(f"{num1}+{num2}={result}")
        case 2:
            if(num1<num2):
                raise Exception(f"Enter a value where {num1}  greater than {num2}")
            result=num1-num2
            print(f"Result:{result}")
            history.append(f"{num1}-{num2}={result}")
        case 3:
            result=num1*num2
            print(f"Result:{result}")
            history.append(f"{num1}*{num2}={result}")
            
        case 4:
            try:
                result=num1/num2
                print(f"Result:{result}")
                history.append(f"{num1}/{num2}={result}")
            except ZeroDivisionError:
                print(f"cannot divide {num1} by {num2}->division by zero")
        case 5:
            try:
                result=num1%num2
                print(f"Result:{result}")
                history.append(f"{num1}%{num2}={result}")
            except ZeroDivisionError:
                print(f"cannot divide {num1} by {num2}->division by zero")        
        case 6:
            try:
                result=num1//num2
                print(f"Result:{result}")
                history.append(f"{num1}//{num2}={result}")
            except ZeroDivisionError:
                print(f" Cannot divide {num1}by {num2}-division by zero") 
        case 7:
            result=num1**num2
            print(f"Result:{result}")
            history.append(f"{num1}^{num2}={result}")
        case _:
            print("Enter valid number")


def input_Numbers():
    n=int(input("Enter the number:"))
    m=int(input("Enter the number:"))
    return n,m


while True:  
        try:          
           n,m= input_Numbers()
           Confirm=input('Do you want to change->\t"YES"\t"NO":\n')
           if(Confirm.lower()=="yes"):
              n,m= input_Numbers()
           
           choice=int(input("Enter the choice you want\n 1.Add\t2.Subtraction\t3.Multiplication\t4.Division\t5.Modulo\t6.Integer_division\t7.Power\n your choice:"))
           calc(n,m,choice)
        except ValueError:
            print("Sorry,Enter a valid number!!!")
        except Exception as e:
            print("Error",e)
        finally:
            view=input("Do you want history\tYES\tNO:\n").lower()
            if(view=="yes"):
                print("History")
                for x in history:
                    print(x)
            clr=input("Clear history:\tYes\tNo:").lower()
            if(clr=="yes"):
                history.clear()
                print("History cleared")
            restart=input("Do you want to continue\nYES or NO:\n")
            if(restart.lower()!="yes"):
                print("Calculator Exited!!!")
                break
                 