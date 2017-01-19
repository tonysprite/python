#!/usr/bin/python
#-*- coding:UTF-8 -*-

dict={"ele":1,"elf":"我是中国字"};
print dict['ele'];
print "\n\r";
print dict['elf'];
dict['ele']='我变了';
print "\n\r";
print dict['ele'];
dict.clear();
print "\n\r";
if dict:
	print 'dict still exists';
else:
	print 'dict dose not exist any more';
