str="This ia a string "
str2=' this is a string '
str3=""" this ia a  string also """
# by using /n be can add a string to the next line 

#Slicing 
# Accessing part of a  string 
#   str[ staring_indx:ending_idx]  start wala index print hoga or end wala index print ni hoga 
str4="Hello world"
print(str4[0:6])

# you can also use backward slicing by using -ve indexing
print(str4[-6:-1])

# String Function
str5 = "i am a  coder "
str5.endswith("er")   # search the last string word and then give true or false value 
str5.capitalize()  # capitalize the first letter of the first word 
str5.replace( old,new) # replace the old word by the new one
str.find(word) # return  1st index of  the search word   

# negative indexes only vaild for slicing 
