import timeit
import emojistools
from sys import argv

script, fi = argv
start = timeit.timeit()
emojis = emojistools.loadEmojis()
end = timeit.timeit()
print (end - start)

openfile = open(fi)
allLines = openfile.read()
openfile.close()

start = timeit.timeit()
i = 0
for line in allLines:
  if(emojistools.containsEmojis(line,emojis)):
    i+=1

end = timeit.timeit()
print (i)
print (end - start)
