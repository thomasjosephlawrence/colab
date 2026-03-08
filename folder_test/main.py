# 1. the "tool" - function definition
def repeat(s, exclaim):
    result = s + s + s
    if exclaim:
        result = result + "!"
    return result
# 2. The "work' *the main function*
def main():
    print(repeat("Yay", False))
    print(repeat("Woo Hoo", True))

# 3. The "starter" : The boilerplate
if __name__ == "__main__":
    main()      