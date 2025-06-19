# buggy_script.py

def divide(a, b):
    return a / b

def say_hello(name)
    print("Hello, " + name)

def process_list(items):
    total = 0
    for item in items:
        total += item
    return total / len(item)  # should be len(items)

if __name__ == "__main__":
    say_hello("Krithika")
    print("Result of division:", divide(10, 0))  # ZeroDivisionError
    print("Processed list average:", process_list([1, 2, 3, 4]))
