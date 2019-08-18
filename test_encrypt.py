from encrypt import colours, format_en_files, format_de_files


def test_format_en_files():
    bld = colours['BOLD']
    end = colours['END']

    output = format_en_files([
        {'key': 'key1', 'file': 'file1'},
        {'key': 'key2', 'file': 'file2'}
    ])

    assert output == 'file `' + bld + 'file1' + end + '` with key `' + bld + 'key1' + end + \
        '`\n  file `' + bld + 'file2' + end + '` with key `' + bld + 'key2' + end + '`'

    print('test_format_en_files was successful!')


def test_format_de_files():
    bld = colours['BOLD']
    end = colours['END']

    files = [
        {'key': 'key1', 'file': 'file1'},
        {'key': 'key2', 'file': 'file2'}
    ]

    output = format_de_files(files)

    assert output == 'Number of decrypted files: ' + str(len(files)) + \
        '\n  file `' + bld + 'file1' + end + '`' + \
        '\n  file `' + bld + 'file2' + end + '`'

    print('test_format_dec_files was successful!')


# running unit tests
test_format_en_files()
test_format_de_files()
