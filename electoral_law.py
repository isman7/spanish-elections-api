# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:56:19 2015

@author: a.fajula
"""

from __future__ import division
import numpy as np

class ley_electoral(object):
    
    def __init__ (self, votes, representatives, ham='DHont', corte=0.03):
        
        #self.info = basic_info()
        self.votes=votes
        self.total_votes=0
        
        for i in self.votes:
            self.total_votes+=i
        
        self.representatives=representatives
        self.ham=ham                                    #Highest avarage method
        self.minratio=corte
        
        self.VoteCalcs()
        self.HamSelection()
        self.ElectedCalc()

        
    def VoteCalcs(self):
        self.threshold=self.total_votes*self.minratio
        self.valid_votes=np.array([score for score in self.votes if score>=self.threshold])
        self.chart=np.zeros((self.valid_votes.size,self.representatives))
        
    def HamSelection(self):
        
        if self.ham=='DHont':
            self.DHont()
        elif self.ham=='Sainte_Lague':
            self.Sainte_Lague()
        
    def DHont(self):
        #
        # D'Hont highest avarage method
        #
        for j in xrange(self.representatives):
            self.chart[:,j]=self.valid_votes[:]/(j+1)

    def Sainte_Lague(self):
        #
        #  Sainte-Laguë Highest avarage method, 
        #
        for j in xrange(self.representatives):
            self.chart[:,j]=self.valid_votes[:]/(2*j+1)
            
    def ElectedCalc(self):
        
        sorted_chart=np.argsort(-self.chart, axis=None)
        elected_chart=(sorted_chart[:self.representatives])
        self.elected=np.uint8(elected_chart[:]/self.representatives)
        
        
        