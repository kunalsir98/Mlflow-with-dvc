with open("artifact.txt","r") as f:
    text=f.read()

with open("artifact.txt","w")as f:
    text=f.write(text+"i have done")    


print(text)    
print("stage 3 has been ended")