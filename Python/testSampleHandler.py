#
from sampleHandler import SampleHandler

print(f'{ SampleHandler.is_file_exists( "C:/Temp/test.txt" )= }')
print(f'{ SampleHandler.is_file_exists( "C:/Temp/test_not_exists.txt" )= }')
print(f'SampleHandler.get_my_data_set( "KIA", 9 )=')
print(f'{ SampleHandler.get_my_data_set( "KIA", 9 ) }')