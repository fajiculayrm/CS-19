print('Enter Text')
enteredText = input()

print('Enter start number')
startNumber = input()

print('Enter end number')
endNumber = input()

toSlice = slice(int(startNumber) + 1, int(endNumber))

print(enteredText[toSlice])