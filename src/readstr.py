#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Reads structure files: PDB, multi model PDB, DCD, XTC
See LICENSE
"""

# Built-in/Generic Imports
import os
import sys

# import other Libs
from Bio.PDB.PDBParser import PDBParser 

# my modules

__author__ = 'Houcemeddine Othman'
__copyright__ = 'Copyright 2019, AYDA'
__license__ = 'MIT License'
__maintainer__ = 'Houcemeddine Othman'
__email__ = 'houcemoo@gmail.com'
__status__ = 'in progress'


class PdbRead:
	"""docstring for PdbReadWrite"""
	def __init__(self):
		pass
		
	def read_pdb(self, PdbFile):
		parser = PDBParser( QUIET=True )
		self.structure = parser.get_structure('S', PdbFile )
		number_of_models = len(self.structure)
		first_structure = self.structure[0]
		self.chain_ids = []
		for chain in first_structure: 
			self.chain_ids.append(chain.id)
		print( """Reading structure {0}
	Number of models: {1} 
	Number of chains {2}""".format(PdbFile, len(self.structure), len(self.chain_ids)  ) )
		return self.structure, self.chain_ids

		

pdb = '../../../6o7g.pdb'

myfile =  PdbRead()
myfile.read_pdb(pdb)