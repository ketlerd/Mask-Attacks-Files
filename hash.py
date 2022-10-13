"""
A simple python script to hash a given file with NTLM
and write it out to an output file

David Ketler -- Specops Software an Outpost 24 company, 2022

"""
import hashlib,binascii
import sys

if(len(sys.argv) < 2):
    print("Please include the filename of the wordlist to hash")
    print("ie: python hash.py rockyou.txt")
    exit()

with open(sys.argv[1], "r", encoding='latin-1') as f:
    with open("hashes.txt", "w") as out:
        for line in f:
            hash = hashlib.new('md4', line.rstrip('\n').encode('utf-16le')).hexdigest()
            out.write(hash + "\n")
            line = f.readline()
