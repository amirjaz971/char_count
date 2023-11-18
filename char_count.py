print("hello this progam counts the number of 'a' character ")
text=input("please enter the text: ")
count=0
a=0
while text[a]!=".":

 if text[a]=="a":
    count+=1
 a+=1

   
   
print("the count of 'a' in this text is: "+str(count))    