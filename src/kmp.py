def kmp(text, pattern):
    '''
    Melakukan searching pattern pada text yang ada
    '''
    text = text.lower()
    pattern = pattern.lower()
    n = len(text)
    m = len(pattern)

    fail = border(pattern)
    # print(n,m)
    i = 0
    j = 0
    while (i < n):
        if (text[i] == pattern[j]):
            if (j == m-1):
                return i-m+1
            i += 1
            j += 1
        elif (j > 0):
            j = fail[j-1]
        else:
            i += 1     
    return -1

def border(pattern):
    fail = ["" for i in range(len(pattern))]
    fail[0] = 0

    m = len(pattern)
    j = 0
    i = 1
    while (i < m):
        if (pattern[i] == pattern[j]):
            fail[i] = j+1
            i += 1
            j += 1
        elif (j > 0):
            j = fail[j-1]
        else:
            fail[i] = 0
            i += 1
    return fail

if __name__ == "__main__":
    text = input("Text: ")
    pattern = input("Pattern: ")
    idx = kmp(text,pattern)
    print("Kata text ditemukan di indeks ke "+str(idx)+" pada pattern")
    