
#FILE HANDLING by Jude Cafranca

text_file = open("text.txt",'w')
text_file.write("I have to pass this Subject")
text_file.close()
text_file = open("text.txt",'a')
text_file.write(" to make my parents proud")
text_file.close()


# to display in run!
text_file = open("text.txt",'r')
print(text_file.read())
text_file.close()