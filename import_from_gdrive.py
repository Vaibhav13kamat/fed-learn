# this downloads the model from the drive 
import gdown

file_id = "https://drive.google.com/file/d/1-Ba3UlzLKhtOGuffVbxVPBiymaPd8hYH/view?usp=sharing"
output_file = "reuben_model_innception.h5"

gdown.download(file_id, output_file, quiet=False, fuzzy=True)