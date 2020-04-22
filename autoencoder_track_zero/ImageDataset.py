import os
import numpy as np
from PIL import Image
from torch.utils.data import Dataset

class ImageDataset(Dataset):
	def __init__(self, imgs_dir):
		self.imgs_dir = imgs_dir
		self.imgs_names = sorted(os.listdir(imgs_dir))

	def __len__(self):
		return len(self.imgs_names)

	def __getitem__(self, idx):
		img = np.array(Image.open(self.imgs_dir + '/' + self.imgs_names[idx]))
		return img


