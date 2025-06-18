def add(a, b):
    return a + b

def divide(a, b):
     a / b  # ⚠️ will raise ZeroDivisionError if b = 0

if __name__ == "__main__":
    print("Add: ", add(2, 3))
    print("Divide: ", divide(4, 2))
