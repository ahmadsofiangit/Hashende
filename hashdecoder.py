# No AI involved at this code, Originally made by human hand.
# AUTHOR: Retro Breado
# PUBLISH ON: GITHUB
# PROJECT TYPE: PERSONAL
# STATUS: PUBLIC

# Import python libries
import hashlib
from sys import argv
import time

err_msg_invalid_arg = "[!] Invalid argument please using -h for more."
err_msg_file_not_found = "was not found, Please try again and give the right path of the file."
help_commands = f"Usage:\n\tpython3 {argv[0]} [hashed file] [wordlist file]\n\tpython3 {argv[0]} hash.txt wordlist.txt\n\nArgument options:\n\t-h | Showing help commands."
fail_msg2 = "\n[!] Trying to guess the hash with the wordlist but fail, I want to tell u never give up! try use other wordlist!"
label_info = "\n" + "Some infomation about hash." + "\n"
complete_msg = "Text plain"
complete_msg2 = "\n"

class info():
    status_info = False

class hashtype():
    hashes = (
            "md5",
            "sha1",
            "sha224",
            "sha256",
            "sha384",
            "sha3_224",
            "sha3_256",
            "sha3_384",
            "sha3_512",
            "sha512"
        )
    
try:
    argv[1]
except IndexError:
    print(err_msg_invalid_arg)
    exit()

#        print(f"\nHash: '{hash_files.strip()}'")
#            print(f"{complete_msg}: '{word.strip()}'")
#            print(f"{label_info}Hash type: '{hashtype.hashes[2]}'\nLength: '{len(hash_files)}'")
#

def guessing_hash_with_wordlist():
    try:
        open(argv[1]).read()
    except FileNotFoundError:
        print(f"[!] The hash file name '{argv[1]}' {err_msg_file_not_found}")
        exit()
    try:
        open(argv[2]).read()
    except FileNotFoundError:
        print(f"[!] The wordlist file name '{argv[2]}' {err_msg_file_not_found}")
        exit()
    
    hash_files = open(argv[1]).read()
    wordlist_file = open(argv[2])

    for word in wordlist_file:
        print(f"Just starting to guessing the hash with [{word.strip()}]...")
        time.sleep(0.50)

        if hashlib.md5(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[0]}")
            info.status_info = True
            break
        elif hashlib.sha1(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[1]}")
            info.status_info = True
            break
        elif hashlib.sha224(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[2]}")
            info.status_info = True
            break
        elif hashlib.sha256(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[3]}")
            info.status_info = True
            break
        elif hashlib.sha384(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[4]}")
            info.status_info = True
            break
        elif hashlib.sha3_224(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[5]}")
            break
        elif hashlib.sha3_256(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[6]}")
            info.status_info = True
            break
        elif hashlib.sha3_384(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[7]}")
            info.status_info = True
            break
        elif hashlib.sha3_512(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[8]}")
            info.status_info = True
            break
        elif hashlib.sha512(word.strip().encode()).hexdigest() in hash_files:
            print(f"\nEncoded Hash: '{hash_files.strip()}'\nDecoded Hash: {word.strip()}\nHash Type: {hashtype.hashes[9]}")
            info.status_info = True
            break

    if info.status_info == True:
        print("\n[!] Successfully guessed the hash.")
    else:
        print(fail_msg2)

if argv[1] == "-h":
    print(help_commands)
else:
    guessing_hash_with_wordlist()

