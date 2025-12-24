# def is_prime(n):
#     for k in range(2,round(n/2)):
#         if n%k==0:
#             return False
#         return True
    

# is_prime(100)

def fib(n):

    a,b= 0,1
    for _ in range(n):
        print(a, end=' ')
        a,b= b, a+b

fib(5)


if __name__ =="__main__":
        import sys
        
        fib(int(sys.argv[1]))
        fib(int(sys.argv[1]))