bookPath = "books/frankenstein.txt"

def readContent(input):
    with open(input) as f:
        return f.read()

def countWords(input):
    words = input.split()
    return len(words)

def countChars(input):
    lenght = len(input)
    return lenght


def toLower(input):
    i = countChars(input)
    c = True
    b = bytearray(input, 'ascii')
    while c:
        i -= 1
        if (b[i] >= 65) and (b[i] <= 90):
            b[i] += 32
        if i == 0:
            c = False
    return b.decode("ascii")

def createDict(input):
    h = {}
    i = countChars(input)
    c = True
    a = toLower(input)
    b = bytearray(a, 'ascii')
    while c:
        i -= 1
        h[chr(b[i])] = 0
        if i == 0:
            c = False
    c = True
    i = countChars(input)
    while c:
        i -= 1
        h[chr(b[i])] += 1
        if i == 0:
            c = False
    return h

def main():
    content = readContent(bookPath)
    d = createDict(content)
    s = sorted(d.items( ), key=lambda x: x[1], reverse=False)
    l = len(s)
    b = True
    print(countWords(content), " Words")
    print(countChars(content), " Characters\n")
    while b:
        l -= 1
        print(f"Character: '{s[l][0]}'\tOccurrence: {s[l][1]}")
        if l == 0:
            print("-- END --")
            exit()
main()
