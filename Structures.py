letters = ['K','I','M','B','E','R','L','Y',
                'A','N','N','S','O','R','I','A',
                'B','K','I','M','E','L','Y',
                'F','X','H','Z','S','O','N','G' ,
                'I','N','E','E','R','I','N','G']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(3)
print ("letters repeated")
print(repeat)