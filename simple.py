
# Import module functions to create key, encrypt and decrypt files
import modules.VU_encrypt as VU_encrypt
import os

# initialise variable
a = 0
list_encrypted_files_keys = []
list_decrypted_files = []

# menu and options
while a != 4:
    print("1. Make Key")
    print("2. Encrypt File")
    print("3. Decrypt file")
    print("4. Exit")

    try:
        a = int(input("press 4 to exit or a valid option to continue [1-3]: \n"))
    except Exception as e:
        print("\n Not Valid Menu Option [1,2,3,4] please, Try again \n")
        continue

    if a == 1:
        try:
            my_key = input("Enter Key Name: ")
            if os.path.isfile(my_key):
                print("File exist")
            else:
                VU_encrypt.make_key(my_key)
                print("Encryption key was created")
        except Exception as e:
            s, r = getattr(e, 'message', str(e)), getattr(e, 'message', repr(e))
            print('s:', s, 'len(s):', len(s))
            print('r:', r, 'len(r):', len(r))

    elif a == 2:
        try:
            my_file = input("Enter file name to be encrypted: ")
            my_enc = input("Enter name of new encrypted file: ")
            my_key = input("Enter key name to be used to encrypt file: ")
            if os.path.isfile(my_enc):
                print("File exist")
            else:
                VU_encrypt.encrypt_file(my_file, my_enc, my_key)
                list_encrypted_files_keys.append('file: ' + my_enc + ' - Key ' + my_key)
                print("Encrypted file was created")
        except Exception as e:
            s, r = getattr(e, 'message', str(e)), getattr(e, 'message', repr(e))
            print('s:', s, 'len(s):', len(s))
            print('r:', r, 'len(r):', len(r))

    elif a == 3:
        try:
            my_enc = input("Enter file name to be decrypted: ")
            my_file = input("Enter name of new decrypted file: ")
            my_key = input("Enter key name to be used to decrypt file: ")
            if os.path.isfile(my_file):
                print("File exist")
            else:
                VU_encrypt.decrypt_file(my_enc, my_file, my_key)
                list_decrypted_files.append(my_enc)
                print("Decrypted file was created")
        except Exception as e:
            s, r = getattr(e, 'message', str(e)), getattr(e, 'message', repr(e))
            print('s:', s, 'len(s):', len(s))
            print('r:', r, 'len(r):', len(r))
    elif a == 4:
        print("Files encrypted: {}".format(list_encrypted_files_keys))
        print("Number of decrypted files {le} files {li}".format(le=len(list_decrypted_files), li=list_decrypted_files))
        print("Exit the Program")
    else:
        print("\n Not Valid Menu Option [1,2,3,4] please, Try again \n")
