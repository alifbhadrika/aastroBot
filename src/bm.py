def buildLastArray(stringInput):
    last = {}
    
    count = 0
    for char in stringInput:
        last[char] = count
        count += 1

    return last

def bm(text,stringInput):
    text = text.lower()
    stringInput = stringInput.lower()
    last = buildLastArray(stringInput)
    n = len(text)
    m = len(stringInput)
    i = m-1
    j = m-1

    if (i>n-1):
        return -1
    
    while (i<=n-1):
        if (stringInput[j] == text[i]):
            if (j==0):
                return i
            else:
                i -= 1
                j -=1
        else:
            lastOccurence = 0
            if text[i] in last:
                lastOccurence = last.get(text[i])
            else:
                lastOccurence = -1
            i = i + m - min(j,1+lastOccurence)
            j = m-1

    return -1

'''
text = "akuseringpergikepasaruntukbeliayamgorengdepanrumah"
pat = "ayamgoreng"
hasil = bm(text,pat)
print(hasil)
'''
if __name__ == "__main__":
    text = "test"
    pattern = "deadline"
    print(bm(text, pattern))