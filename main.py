def palindrome(word):
    end = False
    if word == " ":
        end = False
    else:
        stripped = word.strip()
        lowered = stripped.lower()
        num = lowered.rfind(lowered)
        

        if num == -1:
            end = False
        else:
            end = True

    return end

user_in = input()
print(palindrome(user_in))

    

