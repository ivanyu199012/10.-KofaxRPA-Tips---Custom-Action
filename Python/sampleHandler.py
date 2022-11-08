#
from pathlib import Path
import pandas as pd

class SampleHandler:

	@staticmethod
	def is_file_exists( path : str ):
		return "true" if Path( path ).exists() else "false"

	@staticmethod
	def get_my_data_set( car : str, passing : int ):
		mydataset = {
			'cars': ["BMW", "Volvo", "Ford", car],
			'passings': [3, 7, 2, passing]
		}
		return 	pd.DataFrame( mydataset ).to_string()