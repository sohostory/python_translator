from translate import Translator

translator = Translator(to_lang='ko')

try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('test-ko.txt', mode='w') as new_file:
            new_file.write(translation)
        print("Translation completed.")

except FileNotFoundError as e:
    print('File not found.')
