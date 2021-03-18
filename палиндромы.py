
def ispal(text):
    return text==text[::-1]

def main():
    text = input()
    pals = [""]
    lvl = 2
    result = ""

    while lvl<len(text):
        ch = 0
        while ch+lvl <= len(text):
            if ispal(text[ch:ch+lvl]):
                pals.append(text[ch:ch+lvl])
            ch += 1
        if pals != []:
            break
        lvl += 1

    for pal in pals:
        if pal>result:
            result = pal
    print(result)

main()
