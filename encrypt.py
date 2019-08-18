# Migalys Pavon, 2018-08-13, encrypt program
# main module
# importing the functions define on utils and menu this program shows a menus for the user to
# create key by entering key filename
# encrypt files by choosing a key and entering clear filename and encrypted filename
# if no key first create the key
# decrypt files by choosing a key and entering  encrypted filename and decrypted filename
# if no key first create the key and encrypt a file
# if errors are encounter display messages
# on exit displays total encrypted files, file names and keys, and total of decrypted files with file names

from utils import init_state, create_key, encrypt, decrypt
from menu import main_menu

colours = {
    'OPTION': '\033[94m',
    'WARNING': '\033[93m',
    'ERROR': '\033[91m',
    'END': '\033[0m',
    'BOLD': '\033[1m'
}

# dictionary to keep program state
state = {
    'keys': [],
    'encrypts': [],
    'decrypts': []
}


# format encrypted filename and key name from state['encrypts']
def format_en_files(files):
    bld = colours['BOLD']
    end = colours['END']
    output = ''
    files_count = len(files)

    for idx, file in enumerate(files, start=1):
        output += 'file `{}` with key `{}`{}'.format(
            bld + file['file'] + end,
            bld + file['key'] + end,
            '\n  ' if files_count > idx else ''
        )

    return output


# format decrypted files name from state['decrypts']
def format_de_files(files):
    bld = colours['BOLD']
    end = colours['END']
    output = ''
    dec_files = ''
    files_count = len(files)

    for idx, file in enumerate(files, start=1):
        dec_files += 'file `{}`{}'.format(
            bld + file['file'] + end,
            '\n  ' if files_count > idx else ''
        )
    output += 'Number of decrypted files: {}{}'.format(files_count, '\n  ') + dec_files

    return output


# prints state output
def print_state():
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    # print('Keys: \n  {b}{k}{e}'.format(
    #     b=bld,
    #     k='{e},\n  {b}'.format(e=end, b=bld).join(state['keys']),
    #     e=end
    # ))
    print('Encrypted files: \n  ' + format_en_files(state['encrypts']))
    print('Decrypted files: \n  ' + format_de_files(state['decrypts']))
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


# main process
def main():
    option = ''

    state['keys'] = init_state()

    while option != 'x':
        try:
            option = main_menu(colours)

            if option == 'c':
                key = create_key(colours)
                if key:
                    state['keys'].append(key)

            elif option == 'e':
                if not len(state['keys']):
                    key = create_key(colours)
                    if key:
                        state['keys'].append(key)

                if state['keys']:
                    encoded = encrypt(state['keys'], colours)
                    if encoded:
                        state['encrypts'].append(encoded)

            elif option == 'd':
                if not len(state['keys']):
                    print('There are not keys, please create one and encrypt a file.')
                else:
                    decoded = decrypt(state['keys'], colours)
                    if decoded:
                        state['decrypts'].append(decoded)

            print()
        except Exception as e:
            s, r = getattr(e, 'message', str(e)), getattr(e, 'message', repr(e))
            print('s:', s, 'len(s):', len(s))
            print('r:', r, 'len(r):', len(r))
    print_state()


if __name__ == '__main__':
    main()
