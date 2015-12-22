# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:56:19 2015

@author: a.fajula
"""

from __future__ import division
import numpy as np

class ley_electoral(object):
    
    def __init__ (self, votos, representantes, metodo='DHont', corte=0.03):
        
                #self.info = basic_info()
        self.votes=votos
        self.total_votes=0
        
        for i in self.votes:
            self.total_votes+=i
        
        self.representatives=representantes
        self.ham=metodo #Highest avarage method
        self.minratio=corte
        self.threshold=self.total_votes*self.minratio
        
        self.valid_votes=np.array([score for score in self.votes if score>=self.threshold])
        self.chart=np.zeros((self.valid_votes.size,self.representatives))
        
        if self.ham=='DHont':
            self.DHont()
        elif self.ham=='Sainte_Lague':
            self.Sainte_Lague()
        
        self.elected=np.argsort(-self.chart, axis=None)
        
        self.elected=(self.elected[:self.representatives])
        self.elected[:]=np.uint8(self.elected[:]/self.representatives)
        
        
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