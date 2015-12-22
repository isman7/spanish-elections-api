# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:56:19 2015

@author: a.fajula
"""

from __future__ import division
import numpy as np

def dhont(votes, representatives):
    
    total_votes=0
    for i in votes:
        total_votes+=i
    #spanish threshod 3%
    dhont_threshold=total_votes*0.03
    
    valid_votes=np.array([score for score in votes if score>=dhont_threshold])
    
    dhont_chart=np.zeros((valid_votes.size,representatives))
    
    for j in xrange(representatives):
        dhont_chart[:,j]=valid_votes[:]/(j+1)
    
    elected=-np.sort(-dhont_chart, axis=None)
    
    return elected[:representatives]