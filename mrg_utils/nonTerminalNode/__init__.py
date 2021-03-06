#    nonTerminalNode.py
#    Class definition for NonTerminalNode
#
#    Created by Robert Elwell, University of Texas at Austin, Department of Linguistics
#    http://comp.ling.utexas.edu/relwell
#
#
#    This file is part of mrg_utils.py.
#
#    mrg_utils.py is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    mrg_utils.py is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with mrg_utils.py.  If not, see <http://www.gnu.org/licenses/>.


from ..node import *
from ..terminalNode import *

class NonTerminalNode(Node):
    def __init__(self, aList, aParent, aSentCount):
        Node.__init__(self, aList, aParent, aSentCount)
        self.children = self.populateChildren(aList)
        self.string = self.getString()
        self.head = self.getHead()
        self.termHead= self.getTermHead()
        
    def getString(self):
        return ' '.join([i.string for i in self.children])
        
    def populateChildren(self, aList):
        children = []
        for i in aList:
            if type(i) == list:
                if self.terminalCheck(i) == True:
                    children.append(TerminalNode(i, self, self.index))
                else:
                    children.append(NonTerminalNode(i, self, self.index))
        for i in range(0, len(children)):
            try:
                children[i].oneRight = children[i+1]
            except:
                pass
            if i > 0:
                children[i].oneLeft = children[i-1]
            children[i].oneUp = self
        return children
            
            
    def getTermHead(self):
        if self.head.isTerminal:
            self.head.headOf.append(self)
            return self.head
        else:
            return self.head.termHead