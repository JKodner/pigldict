print "Converting the entire English Dictionary into Pig Latin..."
words = []
f = open('/usr/share/dict/words')
x = open("text.txt", "w")
for itm in f.readlines():
    itm = itm[0].upper() + itm[1:]
    words.append(itm.strip())
for i in words:
    pyg = "ay"
    i = i
    first = i[0]
    if len(i) > 0 and i.isalpha():
        if first in "aeiou":
            new_word = i + pyg
            new_word = new_word[0].upper() + new_word[1:]
            phrase = "%s, %s" % (i, new_word)
            # x.write(str(phrase) + "\n")
        else:
            new_word = i[1:] + i[0].lower() + pyg
            new_word = new_word[0].upper() + new_word[1:]
            phrase = "%s, %s" % (i, new_word)
            # x.write(str(phrase) + "\n")
x.close()
f.close()




