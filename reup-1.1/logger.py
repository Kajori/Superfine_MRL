'''This module contains logging utility functions for ReUP.'''

###########################################################################
##    Copyright 2010 Rahul Suri and Tandy Warnow.
##    This file is part of ReUP.
##
##    ReUP is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    ReUP is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with ReUP.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################

import sys

class ReUPLogger(object):
    '''This class logs useful information.'''

    def __init__(self, fileStream=sys.stderr):
        self.unresolvablePolytomies = 0
        self.resolvablePolytomies = 0
	self.fileStream = fileStream;

    def logInfo(self, quartetTrees):
        '''Increment resolvable or unresolvable count.'''
        if not quartetTrees:
            self.unresolvablePolytomies += 1
        else:
            self.resolvablePolytomies += 1

    def printInfo(self):
        '''Print diagnostic info to stderr.'''
        # print info on resolvables
        if self.resolvablePolytomies == 1:
            self.fileStream.write("1 polytomy successfully resolved.\n")
        else:
            self.fileStream.write(`self.resolvablePolytomies` + " polytomies successfully resolved.\n")

        # print info on unresolvables
        if self.unresolvablePolytomies == 0:
            pass
        elif self.unresolvablePolytomies == 1:
            self.fileStream.write("1 polytomy could *not* be resolved.\n")
        else:
            self.fileStream.write(`self.unresolvablePolytomies` + " polytomies could *not* be resolved.\n")
	    
    def logMessage(self, message):
	    self.fileStream.write(message)
	    self.fileStream.flush()
