import hashlib
import termcolor
import time
import sys       
import pyfiglet 



# Typewriter effect
def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

# ASCI Effect
text = pyfiglet.print_figlet(text='passcracker',
                              colors='BLUE')


# User Input 
type_of_hash = str(input("Hash Type (md5,sha1,sha256,sha512): ")).strip()

while type_of_hash.isupper():
    type_of_hash = input('Hash type cannot be in upper case!: ')
    continue
  
valid_input = False
while not valid_input:
    if len(type_of_hash) == 0:
        type_of_hash = input("Hash Type cannot be empty. Please enter again: ").strip()
    else:
        valid_input = True
   
file_path = str(input('Enter file path: '))

hash_to_decrypt = str(input('Enter Hash Value: '))


# Open the File
with open(file_path,) as file:

    for line in file.readlines(): 
# which type of hash it its
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(termcolor.colored(f'[+] Found MD5 password: {line.strip()}', 'green'))
                exit(0)
            
        if type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(termcolor.colored(f'[+] Found SHA1 password: {line.strip()}', 'green'))
                exit(0)
        if type_of_hash == 'sha256':
            hash_object = hashlib.sha256(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(termcolor.colored(f'[+] Found SHA256 password: {line.strip()}', 'green'))
                exit(0)

        if type_of_hash == 'sha512':
            hash_object = hashlib.sha512(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(termcolor.colored(f'[+] Found Password SHA512: {line.strip()}', 'green'))
                exit(0)
    else:
        print(termcolor.colored('[-] Password not in file... ', 'red'))


# Exiting the program    
typing_print('\x1B[3m' "Try harder...",)



    
            




