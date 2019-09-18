# Fibonacci_sqence的改进
import numpy
import time

# imporved Recursion
def Fib_Tail_Recursion(n):
    if n < 3:
        return n
    if List[n - 2] == 0:
        List[n -2] = Fib_Tail_Recursion(n-2)
    if List[n - 1] == 0:
        List[n - 1] = Fib_Tail_Recursion(n-1)
    return List[n - 1] + List [n - 2]    

# tail Recursion compare with Recursion
def Fib2(num1, num2, n):
    if n < 3:
        return n
    if n == 3:
        return num1 + num2
    return Fib2(num2, num1 + num2, n - 1)


def Fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return Fib(n-1) + Fib(n-2)

def Imporved_Fib(n):
    List = [x for x in range(1, n+1)]
    
    if n < 3:
        return List[n - 1]
    else:
        for x in range(3, n+1):
            List[x - 1] = List [x - 2] + List[x - 3]
        return List[n-1]

if __name__ == "__main__":
    Start_time = time.time()
    n = 35
    List = [x-x for x in range(1, n+1)]

    Fib(n)
    print("test Fibonacci_sqence的测试时间为:  %lfS" %(time.time() - Start_time))
    
    Start_time = time.time()
    Fib2(1, 1, n)
    print("test Fibonacci_sqence2 的测试时间为: %lfS" %(time.time() - Start_time))

    Start_time = time.time()
    Fib_Tail_Recursion(n)
    print("test Fib_Tail_Recursion的测试时间为: %lfS" %(time.time() - Start_time))
    
    Start_time = time.time()
    Imporved_Fib(n)
    print("test Improved_Fib_squence的计算时间为:   %lfS" %(time.time() - Start_time))

