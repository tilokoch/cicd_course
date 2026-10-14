def greet(name: str = "") -> str:
    return("Hello" + " " + name)

def calculate(a: int, b: int) -> int:
    return(a+b)

if __name__ == "__main__":
    greet("Joe")