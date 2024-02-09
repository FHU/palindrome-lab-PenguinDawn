
def palindrome(word):
    end = False

    if word == " ":
        end = False
    else:
        stripped = "".join(word.split(" "))
        print(stripped)
        lowered = stripped.lower()
        newStr = ""
        for i in range(len(lowered)-1, -1, -1):
            newStr += lowered[i]
        
        print(newStr, lowered)
        if newStr == lowered:
            end = True
        else:
            end = False

    return end



