text=input("Enter the text \n")
encoded=""
decoded=""
if any(char.isdigit() for char in text):
    i=0
    while i<len(text):
       char=text[i]
       i+=1
       num=""
       while i<len(text) and text[i].isdigit():
          num+=text[i]
          i+=1
       decoded+=char*int(num)
    print("Decoded Output:\n",decoded)
       
else:
    count=1
    for i in range(len(text)-1):
       if text[i]==text[i+1]:
          count+=1
       else:
          encoded+=text[i]+str(count)
          count=1
    encoded+=text[-1]+str(count)
    print("Encoded Output:\n",encoded)


