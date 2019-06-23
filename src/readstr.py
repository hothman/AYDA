#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Reads structure files: PDB, multi model PDB, DCD, XTC
See LICENSE
"""

# Built-in/Generic Imports
import os
import sys
import shutil
from zipfile import ZipFile,  is_zipfile

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
		
	def read_pdb(self, PdbFile, verbose=1):
		parser = PDBParser( QUIET=True )
		self.structure = parser.get_structure('S', PdbFile )
		number_of_models = len(self.structure)
		first_structure = self.structure[0]
		self.chain_ids = []
		for chain in first_structure: 
			self.chain_ids.append(chain.id)
		if verbose == 1 :
			print( """Reading structure {0}
	Number of models: {1} 
	Number of chains {2}""".format(PdbFile, len(self.structure), len(self.chain_ids)  ) )
		return self.structure, self.chain_ids
		
	def read_compressed_pdbs(self, PdbCompressedFiles): 
		if is_zipfile( PdbCompressedFiles ) :
			with ZipFile(PdbCompressedFiles, 'r') as zip: 
				number_of_complexes = len(zip.namelist() )
				zip.extractall("./.temp") 			
				try:
					previous_conformer_chainids = self.read_pdb("./.temp/"+zip.namelist()[0], verbose=0)
					for name in zip.namelist():
						pdb_conformer = self.read_pdb("./.temp/"+name, verbose = 0)
						current_chainids = pdb_conformer[1]
						if current_chainids == previous_conformer_chainids :
							previous_conformer_chainids = current_chainids
						elif current_chainids != previous_conformer_chainids[1]:
							raise IOError("The ensemble of PDBs is not homogenous ")

				except : 
					raise IOError("One of the structures is not of PDB type")
				shutil.rmtree("./.temp")

		else:
			raise IOError( PdbCompressedFiles, "is not a compressed file")

		
