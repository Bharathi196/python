# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:35:43 2019

@author: Bharathi
"""

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)