def repeat(s, exclaim, count=3):
    # Instread of a hardcoded 3, we use the variable 'count'
    result = (s + " ") * count

    if exclaim:
        result = result + '!!!'
    return result

def main():
    user_s = input("Enter a wordy wordy wordy ")
    raw_count = input("How many times u wanna rep? press enty for default:" )
    user_exclaim = input("add exclamation marks? y/n : ").lower() == 'y'

    if raw_count == "":
        print(repeat(user_s, user_exclaim))
    else: 
        print(repeat(user_s, user_exclaim, int(raw_count)))

if __name__ == "__main__":    main()