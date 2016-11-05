__author__ = 'ankit'
import os
from random import shuffle



with open ("dictionary.txt")as f:
	lines=f.readlines()

#print str(lines)
dic=[]
for word in lines:
	flag=0
	if "[" in word:
		start=word.index('[')
	else:
		flag=1
	if "]" in word:
		end=word.index(']')
	
	s=word[:start-1]
	e=word[start+1:end]
	#print s
	#print e
	a=s.split("=")
	if flag==0:
		a.append(e)
	dic.append(a)
shuffle(dic)
for a in dic:
	if len(a[0])<=2:
		dic.remove(a)
	else:	
		#if len(a)<3:
		#	print str(a)
		print str(a[0])+" ==> " +str(a[1])+" ==> " +str(a[2])

print len(dic)


