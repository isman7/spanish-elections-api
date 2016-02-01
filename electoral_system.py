# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:56:19 2015

@author: Raukonim

###############################################################################
#                             Electoral system                                #
#    Creates an object for d'Hont and Sainte-Lague highest avarage methods    #
#                                                                             #
# Definition:                                                                 #
# electoral_system(votes, representatives, ham='DHont', cut=0.03)             #
#                                                                             #
# Parameters                                                                  #
# votes: array_like                                                           #
#       Number of votes to each party.                                        #
# representatives: int                                                        #
#       Number of representatives to elect.                                   #
# ham: str                                                                    #
#       Highest avarage method to asign representatives, DHont or             #
#       Sainte_Lague.                                                         #
# cut: float                                                                  #
#       minimum ratio of votes to be a candicate to the representatives       #
#       assignmnent.                                                          #
#                                                                             #
###############################################################################



"""

from __future__ import division
import numpy as np

class electoral_system(object):
    
    def __init__ (self, votes, representatives, ham='DHont', cut=0.03):
        
        #self.info = basic_info()
        self.votes=votes
        self.total_votes=0
        
        for i in self.votes:
            self.total_votes+=i
        
        self.representatives=representatives
        self.ham=ham                                    #Highest avarage method
        self.minratio=cut
        
        self.VoteCalcs()
        self.HamSelection()
        self.ElectedCalc()

        
    def VoteCalcs(self):
        if self.minratio==0:
            self.threshold=0
        else:
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
        for i in xrange(self.representatives):
            self.chart[:,i]=self.valid_votes[:]/(i+1)

    def Sainte_Lague(self):
        #
        #  Sainte-Laguë Highest avarage method, 
        #
        for i in xrange(self.representatives):
            self.chart[:,i]=self.valid_votes[:]/(2*i+1)
            
    def ElectedCalc(self):
        
        sorted_chart=np.argsort(-self.chart, axis=None)
        elected_chart=(sorted_chart[:self.representatives])
        self.elected=np.uint8(elected_chart[:]/self.representatives)
    
    def basic_info(self):
        
        info='info'
        print info
        
        
        