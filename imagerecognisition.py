import numpy as np
import pandas as pd

from DeepImageSearch import  Index,LoadData,SearchImage

image_list = LoadData().from_folder(folder_list = ["Path"])

Index(image_list).start()

SearchImage().get_similiar_images(image_path=image_list[0],number_of_images=5)

SearchImage().plot_similiar_images(image_path=image_list[0])

