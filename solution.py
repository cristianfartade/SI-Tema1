import secrets

from Crypto.Cipher import AES

f = open("fisiertest.txt", "r")
openFile=f.read().encode()
f.close()
Key='4b3geYrjtXditrex'.encode()
iv='nfiKeKftjsd351is'.encode()


def keyManager():
    K=secrets.token_hex(16).encode()
    cipher=AES.new(Key,AES.MODE_ECB)
    encryptedKey=cipher.encrypt(K)
    return encryptedKey
K1=keyManager()
def nodeA(encryptionType):
    cipher = AES.new(Key, AES.MODE_ECB)
    print("nodeA: cerere cheie")
    key=cipher.decrypt(K1)
    print("nodeA: cheie decriptata")
    if (encryptionType=="ECB"):
        text = CriptareECB(key)
        print("nodeA: trimite mesaj lui nodeB")
        nodeB(text,"ECB")
    elif(encryptionType=="CBC"):
        text = CriptareCBC(key)
        print("nodeA: trimite mesaj lui nodeB")
        nodeB(text,"CBC")
    else: print("criptare invalida")

def nodeB(text,encryptionType):
    cipher = AES.new(Key, AES.MODE_ECB)
    key = cipher.decrypt(K1)
    print("nodeB: primeste fisierul criptat")
    print("nodeB: fisierul primit cu continut criptat:")
    print(text)
    if(encryptionType=="ECB"):
        print(DecriptareECB(text,key).decode("utf-8"))
    elif (encryptionType == "CBC"):
        print(DecriptareCBC(text,key).decode("utf-8"))
    else: print("tipul de criptare dat este invalid")
def CriptareECB(K):
    print("Criptare ECB")
    inputText=[openFile[i:i+16]for i in range(0, len(openFile), 16)]
    Key=b''+K
    cipher=AES.new(Key,AES.MODE_ECB)
    outputText=b""
    for i in range(0,len(inputText)):
        inputText[i]=cipher.encrypt(inputText[i].ljust(16,b" "))
    for i in range(0,len(inputText)):
        outputText=outputText+inputText[i]
    return  outputText

def DecriptareECB(text,K):
    print("Decriptare ECB")
    inputText = [text[i:i + 16] for i in range(0, len(text), 16)]
    cipher = AES.new(K, AES.MODE_ECB)
    outputText = b""
    for i in range(0, len(inputText)):
        inputText[i] = cipher.decrypt(inputText[i].ljust(16, b" "))
    for i in range(0, len(inputText)):
        outputText = outputText + inputText[i]
    return outputText
def CriptareCBC(K):
    print("Criptare CBC")
    inputText = [openFile[i:i + 16] for i in range(0, len(openFile), 16)]
    Key = b'' + K
    cipher = AES.new(Key, AES.MODE_ECB)
    outputText = b""
    iv2=iv
    for i in range(0, len(inputText)):
        xorKey=cipher.encrypt(iv2)
        iv2=xorKey
        inputText[i] = xor(inputText[i].ljust(16, b" "),xorKey)
    for i in range(0, len(inputText)):
        outputText = outputText + inputText[i]
    return outputText
def DecriptareCBC(text,K):
    print("Decriptare CBC")
    inputText = [text[i:i + 16] for i in range(0, len(text), 16)]
    Key = b'' + K
    cipher = AES.new(Key, AES.MODE_ECB)
    outputText = b""
    iv2 = iv
    for i in range(0, len(inputText)):
        Key2 = cipher.encrypt(iv2)
        iv2 = Key2
        inputText[i] = xor(inputText[i].ljust(16, b" "), Key2)
    for i in range(0, len(inputText)):
        outputText = outputText + inputText[i]
    return outputText

def xor(a,b):
    return bytes(a ^ b for a, b in zip(a, b))

if __name__ == '__main__':
    choice=input("Alegeti modul de criptare?\n1: ECB\n2: CBC\n3: Renunta\n")

    while choice!="3":
        if choice=="1":
            nodeA("ECB")
        elif choice=="2":
            nodeA("CBC")
        else:
            print("alegere invalida")
        choice=input()
