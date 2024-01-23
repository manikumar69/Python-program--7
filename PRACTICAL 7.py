fh=open('prac7.txt','w')
word=input("Enter  a word to check for palindrome :")
if(word==word[::-1]):  
      print("The letter is a palindrome")  
      fh.write("The letter is a palindrome")
else:  
      print("The letter is not a palindrome")
      fh.write("The letter not  is a palindrome")
fh.close()