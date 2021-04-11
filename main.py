x = "hello"

def f():

    def g():
       print(x)

    g()
print(f())
