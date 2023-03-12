
f= open("passList.txt","w+")

for i in range(-1,1000000):
     f.write("text"+(str(i+1)).zfill(6)+"\n")

f.close()


