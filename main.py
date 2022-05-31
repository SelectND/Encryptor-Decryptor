import os
from cryptography.fernet import Fernet

#THIS PROGRAM IS NOT A RANSOMWARE ALTHOUGH IT ENCRYPTS FILES! IT HAS A BUILT-IN DECRYPTOR! PLEASE DON'T USE IT AS A RANSOMWARE

if __name__ == '__main__':
    print("WARNING: THIS PROGRAM WILL ENCRYPT ALL THE FILES THAT ARE IN THE DAME FOLDER AS THE PROGRAM! I AM NOT RESPONSIBLE FOR THE POTENTIAL DATA LOSS! be careful")
    #Creates a key, writes it to a file and prints it out; only one-time use; may be commented out
    if(os.path.exists("keyfile.key")):
       None
    else:
        #Creates a key, writes it to a file and prints it out; only one-time use; may be commented out
        key = Fernet.generate_key()
        with open("keyfile.key", "wb") as keyfile:
            keyfile.write(key)
    #Gathers alls the files in the folder and prints them out
    filesInFolder = []
    for currentFile in os.listdir():
        if(currentFile == "main.py" or currentFile == "keyfile.key"):
            continue
        if(os.path.isfile(currentFile)):
            filesInFolder.append(currentFile)    

    #Read the key; Reads and encrypts the file contents; writes the encrypted content to the file

    action = input("What do you want to do? [encrypt/decrypt/newkey]: ")
    if(action == "encrypt"):       
        for currentFile in filesInFolder:
            with open("keyfile.key", "rb") as keyFile:
                key = keyFile.read()

            #Encrypts the content

            with open(currentFile, "rb") as readFile:
                currentContent = readFile.read()
                enc_currentContent = Fernet(key).encrypt(currentContent)
                print(f"{enc_currentContent}\n{currentContent}")

            #Writes the encrypted content to the specific file

            with open(currentFile, "wb") as writeFile:
                writeFile.write(enc_currentContent)
    elif(action == "decrypt"):    
        for currentFile in filesInFolder:
            with open("keyfile.key", "rb") as keyFile:
                key = keyFile.read()

            #Decrypts the content

            with open(currentFile, "rb") as readFile:
                currentContent = readFile.read()
                dec_currentContent = Fernet(key).decrypt(currentContent)

            #Writes the decrypted content to the specific file

            with open(currentFile, "wb") as writeFile:
                writeFile.write(dec_currentContent)
    elif(action == "newkey"):
        #Creates a key, writes it to a file and prints it out; only one-time use; may be commented out
        key = Fernet.generate_key()
        with open("keyfile.key", "wb") as keyfile:
            keyfile.write(key)