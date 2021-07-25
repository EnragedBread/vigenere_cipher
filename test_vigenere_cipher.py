import vigenere_cipher

def test_encoding_a_phrase_with_a_word():
    ciphertext = vigenere_cipher.encode('meet meon tues daye veni ngat seve n.', 'vigilance')
    assert ciphertext == 'hmkb xebp xpmy llyr xiiq tolt fgzz v.'

def test_decoding_a_phrase_with_a_word():
    plaintext = vigenere_cipher.decode('hmkb xebp xpmy llyr xiiq tolt fgzz v.', 'vigilance')
    assert plaintext == 'meet meon tues daye veni ngat seve n.'