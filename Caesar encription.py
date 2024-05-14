import string

def caesar(text,shift,alphabets):
    def shift_alphabets(alpabets):
        return alpabets[shift:] + alpabets[:shift]
    shifted_alphabets = tuple(map(shift_alphabets,alphabets))

    final_alphabets = ''.join(alphabets)
    final_shifted_alphabets = ''.join(shifted_alphabets)

    table = str.maketrans(final_shifted_alphabets,final_alphabets)

    return text.translate(table)

plain_text = "This is a new test, Hello world!"
print(caesar(plain_text,8,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))


plaint_texts = "Hello world!"
shift = 7
shift %= 26
alphabets = string.ascii_lowercase
shifted = alphabets[shift:] + alphabets[:shift]
table = str.maketrans(alphabets,shifted)

encrpyted = plaint_texts.translate(table)
print(encrpyted)