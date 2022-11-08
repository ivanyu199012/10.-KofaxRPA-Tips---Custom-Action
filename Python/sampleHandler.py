#
from pathlib import Path
import pandas as pd

class SampleHandler:

	@staticmethod
	def is_file_exists( path : str ):
		return { 'is_file_exists' : "true" if Path( path ).exists() else "false" }

	@staticmethod
	def get_my_data_set( car : str, passing : str ):
		my_data_set = {
			'cars': ["BMW", "Volvo", "Ford", car],
			'passings': [3, 7, 2, int( passing )]
		}
		return { 'my_data_set' : pd.DataFrame( my_data_set ).to_string() }