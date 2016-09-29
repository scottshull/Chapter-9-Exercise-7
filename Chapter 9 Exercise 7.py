def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def find_triple_double():
    fin = open("C:\Users\scott\Downloads\words.txt")
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print word

print 'These are the words that have'
print 'three consecutive double letters.'
find_triple_double()
print ''
