from stack import Stack

def divide16(decNum):
    s = Stack()

    while decNum > 0:
        rem = decNum % 16
        s.push(lett(rem))
        decNum = decNum//16

    bString = " "
    while not s.is_empty():
        bString = bString + str(s.pop())

    return bString

def lett(rem):
    if rem < 10:
        return rem
    if rem == 10:
        return "A"
    if rem == 11:
        return "B"
    if rem == 12:
        return "C"
    if rem == 13:
        return "D"
    if rem == 14:
        return "E"
    if rem == 15:
        return "F"

print(divide16(668))
