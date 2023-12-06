# membuat fungsi pilihan
def pilihan():
    global menuChoice

    while True:
        print("enkripsi dan dekripsi menggunakan XOR")
        print("\nTipe Input Pesan:")
        print("1. Karakter")
        print("2. Bit")

        menuChoice = input("Pilihlah 1/2: ")

        if menuChoice == '1':
            XORChar()
        elif menuChoice == '2':
            XORBit()
            break
        else:
            print("Pilihan anda tidak sesuai. Silakan pilih sesuai dengan menu!")
    
def checkInputLength():
    global inputMsg, inputKey
    
    while len(inputMsg) <= 5 or len(inputKey) <= 5:
        print("pesan dan Key minimal 5 karakter.")
        inputMsg = input('Masukkan plaintext atau ciphertext: ')
        inputKey = input('Masukkan Key: ')

def equalizeLength():
    global finalKey

    bitToCharLength = int(len(inputMsg)/8)
    if menuChoice == '2':
        if bitToCharLength > len(inputKey):
            tempInputKey = inputKey * (bitToCharLength // len(inputKey) + 1)
            finalKey = tempInputKey[:bitToCharLength]
        else:
            finalKey = inputKey[:bitToCharLength]
    elif menuChoice == '1':
        if len(inputMsg) > len(inputKey):
            tempInputKey = inputKey * (len(inputMsg) // len(inputKey) + 1)
            finalKey = tempInputKey[:len(inputMsg)]
        else:
            finalKey = inputKey[:len(inputMsg)]

def equalizeBitDigit(inputData):
    formatted_binary_chars = [
        format(ord(char), '08b') for char in inputData
    ]

    result = ' '.join(formatted_binary_chars)
    return result


def printMsgAndKey():
    equalizeLength()
    
    if menuChoice == '2':
        print("\nPenyamaan Panjang Pesan dan Kunci:")
        print("Pesan: " + inputMsg)
        print(f"Panjang Karakter Pesan: {int(len(inputMsg)/8)}")
        print("Key: " + finalKey)
        print(f"Panjang Kara    kter Kunci: {len(finalKey)}")
        print("\nBit Pesan:")
        print(printXORResult(inputMsg))
        print("Bit Key:")
        print(equalizeBitDigit(finalKey))
    elif menuChoice == '1':
        print("\nPenyamaan Panjang Pesan dan Kunci:")
        print("Pesan: " + inputMsg)
        print(f"Panjang Karakter Pesan: {len(inputMsg)}")
        print("Key: " + finalKey)
        print(f"Panjang Karakter Kunci: {len(finalKey)}")
        print("\nBit Pesan:")
        print(equalizeBitDigit(inputMsg))
        print("Bit Key:")
        print(equalizeBitDigit(finalKey))

def xorBits(msgBit, keyBit):
    msgBit = msgBit.replace(" ", "")
    keyBit = keyBit.replace(" ", "")
    
    result = ''
    for a, b in zip(msgBit, keyBit):
        if a != b:
            result += '1'
        else:
            result += '0'

    return result

def printXORResult(XORResult):
    xorSplit = [XORResult[i:i+8] for i in range(0, len(XORResult), 8)]
    xorSplitSpace = ' '.join(xorSplit)

    return xorSplitSpace

def bitsToChar(bits):
    chunks = [bits[i:i + 8] for i in range(0, len(bits), 8)]

    chars = [chr(int(chunk, 2)) for chunk in chunks]

    result = ''.join(chars)
    return result

def XORBit():
    global inputMsg, inputKey, finalKey

    print("Tipe Input: Bit")
    print("Pesan setidaknya harus terdiri dari 6 byte yang masing-masing merupakan kode 8 bit")
    inputMsg = input('Masukkan Pesan: ')
    inputKey = input('Masukkan Key: ')

    while len(inputMsg) < 6*8 or len(inputKey) <= 5:
        print("Pesan harus terdiri dari 6 byte (48 Biner Karakter) dan Key harus lebih dari 5 karakter")
        inputMsg = input('Masukkan Pesan: ')
        inputKey = input('Masukkan Key: ')
        
    while len(inputMsg)%8 != 0:
        print("Pesan harus berbentuk ASCII 8 Bit")
        inputMsg = input('Masukkan Pesan: ')
        inputKey = input('Masukkan Key: ')

    printMsgAndKey()

    keyBit = equalizeBitDigit(finalKey)
    msgBit = printXORResult(inputMsg)

    XORResult = xorBits(msgBit, keyBit)
    print("\nHasil XOR dari Bit Pesan dan Bit Key:")
    print(printXORResult(XORResult))

    print("\n========================================================\n")
    print("Hasil enkripsi/dekripsi berhasil ditampilkan di layar\n")
    print("=========================================================\n")

def XORChar():
    global inputMsg, inputKey, finalKey

    print("Tipe Input: Karakter")
    inputMsg = input('Masukkan Pesan: ')
    inputKey = input('Masukkan Key: ')

    checkInputLength()
    printMsgAndKey()

    messageBit = equalizeBitDigit(inputMsg)
    keyBit = equalizeBitDigit(finalKey)

    XORResult = xorBits(messageBit, keyBit)
    print("\nHasil XOR dari Bit Pesan dan Bit Key:")
    print(printXORResult(XORResult))

    print("\n======================================================\n")
    print("Hasil enkripsi berhasil ditampilkan di layar\n")
    print("=======================================================\n")

def main():
    pilihan()

if __name__ == "__main__":
    main()