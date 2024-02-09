
def palindrome(word):

    end = False

    if word == " ":
        end = False

    else:
        stripped = "".join(word.split(" "))
        lowered = stripped.lower()
        newStr = ""
        for i in range(len(lowered) - 1, 0, -1):
            newStr += lowered[i]
        
        if newStr == lowered:
            end = True
        else:
            end = False

    return end

    

