# Module to define function for the menu


# shows menu calls on main_menu
def show_menu(colours):
    opt = colours['BOLD'] + colours['OPTION']
    end = colours['END']
    print('============= MENU =============')
    print('{bc}C{e}reate encryption keys'.format(bc=opt, e=end))
    print('{bc}E{e}ncrypt files using existing keys'.format(bc=opt, e=end))
    print('{bc}D{e}ecrypt files using existing keys'.format(bc=opt, e=end))
    print('E{bc}x{e}it from the menu'.format(bc=opt, e=end))
    print('-------------------------------------------\n')


# defines valid option use by validate_option() and main_menu()
def menu_options():
    return ['c', 'e', 'd', 'x']


# checks valid options
def validate_option(option):
    return option in menu_options()


# shows main menu with colours validates input
def main_menu(colours):
    show_menu(colours)

    possible_options = ', '.join(menu_options())
    option = ''
    is_valid_option = False

    while not is_valid_option:
        option = input('Enter option: ').lower()
        is_valid_option = validate_option(option)
        if not is_valid_option:
            print('{e}Wrong option!{end} {wrn}Possible values are [{opt}]. Please try again.{end}'.format(
                e=colours['ERROR'],
                wrn=colours['WARNING'],
                end=colours['END'],
                opt=possible_options)
            )

    return option


# shows menu for keys selection when more than one key
def keys_menu(keys, colours):
    opt = colours['BOLD'] + colours['OPTION']
    wrn = colours['WARNING']
    end = colours['END']

    print('\n================= KEYS =================')
    while True:
        for idx, key in enumerate(keys, start=1):
            print('({i}) {k}'.format(i=opt + str(idx) + end, k=key))

        print('-------------------------------------------')
        key_opt = input('Select the key number to use or {bc}c{e}ancel: '.format(bc=opt, e=end)).lower()

        if key_opt == 'c':
            return
        else:
            try:
                key_idx = int(key_opt)

                if key_idx <= len(keys):
                    return keys[key_idx - 1]
                else:
                    print('{}Please enter a valid key number{}'.format(wrn, end))
            except ValueError:
                print('{}Please enter a valid key number{}'.format(wrn, end))
