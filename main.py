import vigenere_cipher

def driver():
    a = vigenere_cipher.encode('meet meon tues daye veni ngat seve n.', 'vigilance')
    print(f"{a}")

if __name__ == '__main__':
    driver()