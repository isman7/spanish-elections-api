# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:56:19 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*

interactive(True)
close('all')

def dhont(votes, representatives):
    
    total_votes=0
    for i in votes:
        total_votes+=i
    #spanish threshod 3%
    dhont_threshold=total_votes*0.03
    
    valid_votes=array([score for score in votes if score>=dhont_threshold])
    
    dhont_chart=zeros((valid_votes.size,representatives))
    
    for j in xrange(representatives):
        dhont_chart[:,j]=valid_votes[:]/(j+1)
    
    elected=-sort(-dhont_chart, axis=None)
    
    return elected[:representatives]