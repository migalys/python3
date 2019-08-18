# Module of helper functions
# In this module the functions from VU_encrypt are imported

import os
from cryptography.fernet import InvalidToken
from menu import keys_menu
from VU_encrypt import make_key, encrypt_file, decrypt_file

path_config = {
    'keys_path': 'my_keys',
    'encrypted_files': 'my_encrypted_files',
    'decrypted_files': 'my_decrypted_files'
}


# when run for first time create configuration folders
def init_state():
    # Create paths or skip if the already exist
    for path in path_config.values():
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != 17:
                raise

    return sorted([file for file in os.listdir(path_config['keys_path']) if not file.startswith('.')])
    # return existing keys


# creates keys
def create_key(colours):
    print('\n================== CREATE KEY ===================')

    while True:
        bld = colours['BOLD']
        opt = bld + colours['OPTION']
        wrn = colours['WARNING']
        end = colours['END']

        try:
            key_name = input('Enter key filename or {bc}c{e}ancel: '.format(bc=opt, e=end))
            if key_name in ['c', 'C']:
                return
            if os.path.isfile(path_config['keys_path'] + '/' + key_name):
                print('{}The filename exists. Please, enter a new key name.{}'.format(wrn, end))
            else:
                make_key(path_config['keys_path'] + '/' + key_name)
                print('{b}The key file `{f}` was successfully created.{e}'.format(
                    b=colours['BOLD'],
                    f=path_config['keys_path'] + '/' + key_name,
                    e=colours['END']
                ))

                return key_name
        except (IsADirectoryError, FileNotFoundError):
            print('{}Please enter a valid filename{}'.format(wrn, end))

        except (InvalidToken, ValueError):
            print('{}There was an error creating key, please try again{}'.format(wrn, end))


# encrypts files
def encrypt(keys, colours):
    if len(keys) > 1:
        key = keys_menu(keys, colours)
    else:
        key = keys[0]
        # if there is only one key
        print('The key `{}` will be use to encrypt your file'.format(key))

    if key:
        print('\n================== ENCRYPT ===================')

        bld = colours['BOLD']
        opt = bld + colours['OPTION']
        wrn = colours['WARNING']
        end = colours['END']

        while True:
            try:
                file_2_encode = input('Enter filename to encrypt or {bc}c{e}ancel: '.format(bc=opt, e=end))
                if file_2_encode in ['c', 'C']:
                    return

                encoded_file = input('Enter filename for encrypted output or {bc}c{e}ancel: '.format(bc=opt, e=end))
                if encoded_file in ['c', 'C']:
                    return

                if not os.path.isfile(file_2_encode) and file_2_encode != '':
                    print(
                        '{}The filename does not exist. Please, enter a valid filename to encrypt.{}'.format(wrn, end))

                elif os.path.isfile(path_config['encrypted_files'] + '/' + encoded_file):
                    print(
                        '{}The encrypted filename exists. Please, enter a new encrypted filename.{}'.format(wrn, end))
                else:
                    encrypt_file(
                        file_2_encode,
                        path_config['encrypted_files'] + '/' + encoded_file,
                        path_config['keys_path'] + '/' + key
                    )
                    print('The encrypted file `{}` was successfully created using the key `{}`.'.format(
                        bld + encoded_file + end,
                        bld + key + end
                    ))

                    return {
                        'key': key,
                        'file': encoded_file
                    }
            except (IsADirectoryError, FileNotFoundError):
                print('{}Please enter valid filenames.{}'.format(wrn, end))

            except (InvalidToken, ValueError):
                print('{}Invalid encryption key, please try again{}'.format(wrn, end))


# decrypts files
def decrypt(keys, colours):
    if len(keys) > 1:
        key = keys_menu(keys, colours)
    else:
        key = keys[0]
        # there is only one key
        print('The key `{}` will be use to decrypt your file'.format(key))

    if key:
        print('\n================== DECRYPT ===================')

        bld = colours['BOLD']
        opt = bld + colours['OPTION']
        wrn = colours['WARNING']
        end = colours['END']

        while True:
            try:
                encoded_file = input('Enter filename to decrypt or {bc}c{e}ancel: '.format(bc=opt, e=end))
                if encoded_file in ['c', 'C']:
                    return

                decoded_file = input('Enter filename for decrypted output or {bc}c{e}ancel: '.format(bc=opt, e=end))
                if decoded_file in ['c', 'C']:
                    return

                if not os.path.isfile(path_config['encrypted_files'] + '/' + encoded_file) and encoded_file != '':
                    print(
                        '{}The encrypted file does not exist. Please, enter a new encrypted filename.{}'.format(wrn,
                                                                                                                end))

                elif os.path.isfile(path_config['decrypted_files'] + '/' + decoded_file):
                    print(
                        '{}The decrypted filename exists. Please, enter a new decrypted filename.{}'.format(wrn, end))
                else:

                    decrypt_file(
                        path_config['encrypted_files'] + '/' + encoded_file,
                        path_config['decrypted_files'] + '/' + decoded_file,
                        path_config['keys_path'] + '/' + key
                    )

                    print('A decrypted file `{}` was successfully created.{}'.format(
                        bld + decoded_file,
                        end
                    ))

                    return {
                        'file': decoded_file
                    }
            except (IsADirectoryError, FileNotFoundError):
                print('{}Please enter valid filenames{}'.format(wrn, end))

            except (InvalidToken, ValueError):
                print('{}Wrong encrypted file for the selected key, please try again{}'.format(wrn, end))
