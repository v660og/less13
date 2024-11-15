from spellchecker import SpellChecker


class CaesarsCipher:

    symb_dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcde"\
                "fghijklmnopqrstuvwxyz1234567890 !?."

    def __init__(self, key):
        self._key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if isinstance(key, int):
            self._key = key
        else:
            raise ValueError("Некорректный тип")

    def encrypt(self, message):

        encripted_message = ""

        for letter in message:
            letter_index = CaesarsCipher.symb_dict.find(letter)
            encripted_message += CaesarsCipher.symb_dict[letter_index +
                                                         self._key]

        return encripted_message

    def decrypt(self, message):

        decrypted_message = ""

        for letter in message:
            letter_index = CaesarsCipher.symb_dict.find(letter)
            decrypted_message += CaesarsCipher.symb_dict[letter_index -
                                                         self._key]

        return decrypted_message


def find_key(message):

    for key in range(len(CaesarsCipher.symb_dict)):

        translated = ""

        for symbol in message:
            if symbol in CaesarsCipher.symb_dict:
                symbolIndex = CaesarsCipher.symb_dict.find(symbol)
                translatedIndex = symbolIndex - key
                translated += CaesarsCipher.symb_dict[translatedIndex]

        translated_word_list = translated.split(" ")
        if (
            len(spell.known(translated_word_list)) > 1
            and len(translated_word_list) > 1
        ) or (
            len(spell.known(translated_word_list)) == 1
            and len(translated_word_list) == 1
        ):
            return f"{key}: {translated}"


if __name__ == "__main__":
    spell = SpellChecker()

    print(find_key("o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"))

    cryptor = CaesarsCipher(3)
    dst_path = input('Введите путь к файлу: ')

    print(cryptor.encrypt("The vacation was a success"))
    print(cryptor.decrypt("Wkh.ydfdwlrq.zdv.d.vxffhvv"))

    with open(dst_path, 'w') as file:
        file.write(cryptor.decrypt("Wkh.ydfdwlrq.zdv.d.vxffhvv"))
