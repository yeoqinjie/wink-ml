import re

INFILE = 'story.txt'

try:
    infile = open(INFILE, 'r')

    ins = infile.read()

    ins = re.sub("[^A-Za-z. ]", '', ins)
    ins = ins.split('.')

    word_base = []
    word_dict = {}

    for i in ins:
        j = i.split(' ')
        for k in range(0, len(j)):
            for l in range(0, len(j)):
                if j[k] != j[l]:
                    s = j[k] + " " + j[l]
                    s = s.lower()
                    if s not in word_base:
                        word_base.append(s)
                        v = abs(int(k-l))
                        d = {s: v}
                        word_dict.update(d)
                    else:
                        word_dict[s] += abs(int(k-l))

    outfile = open('out.txt', 'w+')
    for i, j in word_dict.items():
        outfile.write(i + ": " + str(j) + "\n")

except IOError:
    print "No Input File"
