import sqlite3 as sqlite
import re
import math

'''
Original Code: https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter6/docclass.py
'''

def getwords(doc):
  splitter=re.compile('\\W*')
  #print(doc)
  # Split the words by non-alpha characters
  words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
  
  # Return the unique set of words only
  toreturn = dict([(w,1) for w in words])
  return toreturn

class classifier:
  def __init__(self,getfeatures,filename=None):
    # Counts of feature/category combinations
    self.fc={}
    # Counts of documents in each category
    self.cc={}
    self.getfeatures=getfeatures
    
  def setdb(self,dbfile):
    self.con=sqlite.connect(dbfile)    
    self.con.execute('create table if not exists fc(feature,category,count)')
    self.con.execute('create table if not exists cc(category,count)')


  def incf(self,f,cat):
    count=self.fcount(f,cat)
    if count==0:
      self.con.execute("insert into fc values ('%s','%s',1)" 
                       % (f,cat))
    else:
      self.con.execute(
        "update fc set count=%d where feature='%s' and category='%s'" 
        % (count+1,f,cat)) 
  
  def fcount(self,f,cat):
    res=self.con.execute(
      'select count from fc where feature="%s" and category="%s"'
      %(f,cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  def incc(self,cat):
    count=self.catcount(cat)
    if count==0:
      self.con.execute("insert into cc values ('%s',1)" % (cat))
    else:
      self.con.execute("update cc set count=%d where category='%s'" 
                       % (count+1,cat))    

  def catcount(self,cat):
    res=self.con.execute('select count from cc where category="%s"'
                         %(cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  def categories(self):
    cur=self.con.execute('select category from cc');
    return [d[0] for d in cur]

  def totalcount(self):
    res=self.con.execute('select sum(count) from cc').fetchone();
    if res==None: return 0
    return res[0]


  def train(self,item,cat):
    features=self.getfeatures(item)
    # Increment the count for every feature with this category
    for f in features:
      self.incf(f,cat)

    # Increment the count for this category
    self.incc(cat)
    self.con.commit()

  def fprob(self,f,cat):
    if self.catcount(cat)==0: return 0

    # The total number of times this feature appeared in this 
    # category divided by the total number of items in this category
    return self.fcount(f,cat)/self.catcount(cat)

  def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
    # Calculate current probability
    basicprob=prf(f,cat)

    # Count the number of times this feature has appeared in
    # all categories
    totals=sum([self.fcount(f,c) for c in self.categories()])

    # Calculate the weighted average
    bp=((weight*ap)+(totals*basicprob))/(weight+totals)
    return bp

class naivebayes(classifier):
  
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.thresholds={}
  
  def docprob(self,item,cat):
    features=self.getfeatures(item)   

    # Multiply the probabilities of all the features together
    p=1
    for f in features: p*=self.weightedprob(f,cat,self.fprob)
    return p

  def prob(self,item,cat):
    catprob=self.catcount(cat)/self.totalcount()
    docprob=self.docprob(item,cat)
    return docprob*catprob
  
  def setthreshold(self,cat,t):
    self.thresholds[cat]=t
    
  def getthreshold(self,cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]
  
  def classify(self,item,default=None):
    probs={}
    # Find the category with the highest probability
    max=0.0
    for cat in self.categories():
      probs[cat]=self.prob(item,cat)
      if probs[cat]>max: 
        max=probs[cat]
        best=cat

    # Make sure the probability exceeds threshold*next best
    for cat in probs:
      if cat==best: continue
      if probs[cat]*self.getthreshold(best)>probs[best]: return default
    return best

def spamTrain(c):
  # Train For 'Not Spam'
  file1 = open('Training Dataset\\NotSpam1.txt')
  train1 = file1.read()
  c.train(train1, 'Not Spam')
  
  file2 = open('Training Dataset\\NotSpam2.txt')
  train2 = file2.read()
  c.train(train2, 'Not Spam')

  file3 = open('Training Dataset\\NotSpam3.txt')
  train3 = file3.read()
  c.train(train3, 'Not Spam')

  file4 = open('Training Dataset\\NotSpam4.txt')
  train4 = file4.read()
  c.train(train4, 'Not Spam')

  file5 = open('Training Dataset\\NotSpam5.txt')
  train5 = file5.read()
  c.train(train5, 'Not Spam')

  file6 = open('Training Dataset\\NotSpam6.txt')
  train6 = file6.read()
  c.train(train6, 'Not Spam')

  file7 = open('Training Dataset\\NotSpam7.txt')
  train7 = file7.read()
  c.train(train7, 'Not Spam')

  file8 = open('Training Dataset\\NotSpam8.txt')
  train8 = file8.read()
  c.train(train8, 'Not Spam')

  file9 = open('Training Dataset\\NotSpam9.txt')
  train9 = file9.read()
  c.train(train9, 'Not Spam')

  file10 = open('Training Dataset\\NotSpam10.txt')
  train10 = file10.read()
  c.train(train10, 'Not Spam')

  # Train For 'Spam' 
  file11 = open('Training Dataset\\Spam1.txt')
  train11 = file11.read()
  c.train(train11, 'Spam')

  file12 = open('Training Dataset\\Spam2.txt')
  train12 = file12.read()
  c.train(train12, 'Spam')

  file13 = open('Training Dataset\\Spam3.txt')
  train13 = file13.read()
  c.train(train13, 'Spam')

  file14 = open('Training Dataset\\Spam4.txt')
  train14 = file14.read()
  c.train(train14, 'Spam')

  file15 = open('Training Dataset\\Spam5.txt')
  train15 = file15.read()
  c.train(train15, 'Spam')

  file16 = open('Training Dataset\\Spam6.txt')
  train16 = file16.read()
  c.train(train16, 'Spam')

  file17 = open('Training Dataset\\Spam7.txt')
  train17 = file17.read()
  c.train(train17, 'Spam')

  file18 = open('Training Dataset\\Spam8.txt')
  train18 = file18.read()
  c.train(train18, 'Spam')

  file19 = open('Training Dataset\\Spam9.txt')
  train19 = file19.read()
  c.train(train19, 'Spam')

  file20 = open('Training Dataset\\Spam10.txt')
  train20 = file20.read()
  c.train(train20, 'Spam')
