import time


def func(f):
    def wrapper(*args, **kwargs):
        print('Started')
        rv = f(*args, **kwargs)
        print("Ended")
        return rv
    return wrapper

def func2():
    print("i am func2")
@func    
def func3():
    print("i am func3")

@func
def func4(n,m):
    print(n)
    return m

x = func(func2)
func3 = func(func3)
print(x)
x()
func3()
x =func4(5,6)
print(x)


def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        rv = func(*args,**kwargs)
        total = time.time() - start
        print("Time:", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(1000000):
        pass

@timer
def test2():
    for _ in range(1000000):
        time.sleep(2)
    
    
test()
test2()