import Classifier
from subprocess import check_output

'''
Original Code: https://cs532s18.slack.com/files/U8K4TSGJ1/F9Z33U1B6/test.py
'''



c = Classifier.naivebayes(Classifier.getwords)


#remove previous db file

check_output(['rm', 'jpindell.db'])



c.setdb('jpindell.db')


Classifier.spamTrain(c)



#classify files as Spam or Not Spam

file1 = open('Testing Dataset\\Email1.txt')
email1 = file1.read()
print( c.classify(email1) )

file2 = open('Testing Dataset\\Email2.txt')
email2 = file2.read()
print( c.classify(email2) )

file3 = open('Testing Dataset\\Email3.txt')
email3 = file3.read()
print( c.classify(email3) )

file4 = open('Testing Dataset\\Email4.txt')
email4 = file4.read()
print( c.classify(email4) )

file5 = open('Testing Dataset\\Email5.txt')
email5 = file5.read()
print( c.classify(email5) )

file6 = open('Testing Dataset\\Email6.txt')
email6 = file6.read()
print( c.classify(email6) )

file7 = open('Testing Dataset\\Email7.txt')
email7 = file7.read()
print( c.classify(email7) )

file8 = open('Testing Dataset\\Email8.txt')
email8 = file8.read()
print( c.classify(email8) )

file9 = open('Testing Dataset\\Email9.txt')
email9 = file9.read()
print( c.classify(email9) )

file10 = open('Testing Dataset\\Email10.txt')
email10 = file10.read()
print( c.classify(email10) )

file11 = open('Testing Dataset\\Email11.txt')
email11 = file11.read()
print( c.classify(email11) )

file12 = open('Testing Dataset\\Email12.txt')
email12 = file12.read()
print( c.classify(email12) )

file13 = open('Testing Dataset\\Email13.txt')
email13 = file13.read()
print( c.classify(email13) )

file14 = open('Testing Dataset\\Email14.txt')
email14 = file14.read()
print( c.classify(email14) )

file15 = open('Testing Dataset\\Email15.txt')
email15 = file15.read()
print( c.classify(email15) )

file16 = open('Testing Dataset\\Email16.txt')
email16 = file16.read()
print( c.classify(email16) )

file17 = open('Testing Dataset\\Email17.txt')
email17 = file17.read()
print( c.classify(email17) )

file18 = open('Testing Dataset\\Email18.txt')
email18 = file18.read()
print( c.classify(email18) )

file19 = open('Testing Dataset\\Email19.txt')
email19 = file19.read()
print( c.classify(email19) )

file20 = open('Testing Dataset\\Email20.txt')
email20 = file20.read()
print( c.classify(email20) )

