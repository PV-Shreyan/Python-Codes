# Write a program that reads a text file example.txt and counts the number of lines, words, and characters in the file. Print these counts.

with open (r"C:\Users\PV shreyan\OneDrive\Documents\example.txt", 'r') as f1:
    text = f1.read ()
    
    f1.seek (0)
    lines = f1.readlines ()
    
num_lines = len (lines)
num_words = len (text.split())
num_characters = len (text)

print ("No. of lines: ", num_lines)
print ("No. of words: ", num_words)
print ("No. of characters: ", num_characters)
