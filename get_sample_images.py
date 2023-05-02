# image_path = "/content/my_samples/MFGTMP_211115160001_A02f01d0 (1).TIF"
# take_samples(image_path)

from PIL import Image
import glob, os, sys

import random

# path = "/content/my_samples"

images_path = sys.argv[1] # Current Directory

original_images_path = images_path +"\Original_Images"

result_path = images_path + "\Resulting_Samples\\"


# my_images = glob.glob(original_images_path+"/*.TIF")


image_types = ["jpg", "jpeg", "png", "gif","tif"]

my_images = []
for image_type in image_types:
    my_images.extend(glob.glob(f"{original_images_path}/*.{image_type}"))

# print(my_images)


print("Developed By Shck Tchamna (tchamna@gmail.com)")

# crop at 25% (width, height)  50% (width, height) and at 90% (width, height) 
levels_ = [0.25, 0.5, 0.9] 

 # crop at 25% (width, height) and at 90% (width, height) 
levels_ = [0.25, 0.9]

# levels_ = [0.1, .2, .3, .4, 0.5, .6, .7, .8, 0.9, 1] 



def take_samples(image_path, levels=levels_, pixels = 100, n_samples = 3):

  file_name = os.path.basename(image_path)
    
  # image_path = "/content/MFGTMP_211115160001_A02f01d0 (1).TIF"
  # Open the image
  image = Image.open(image_path)

  # Convert the image to RGB mode
  image = image.convert("RGB")

  # Get the width and height of the image
  width, height = image.size

  # Set the pixel levels for the samples
  # levels = [0.25, 0.5, 0.75, 0.9]

  # Loop through the levels and get three random samples for each level
  for level in levels:
      for i in range(n_samples):
          # Calculate the pixel coordinates for the sample
          x = int(width * level)
          y = int(height * level)
          
          # Add some random offset to the coordinates
          x += random.randint(-50, 50)
          y += random.randint(-50, 50)
          
          # Get a 100x100 pixel sample centered on the coordinates
          sample = image.crop((x-pixels/2, y-pixels/2, x+pixels/2, y+pixels/2))
          
          # Save the sample as JPEG
          file_name_new = f"{file_name}_{int(level*100)}_{i+1}.jpg"
          sample.save(result_path+file_name_new, "JPEG")

for img in my_images:
#   print(my_images)

  take_samples(img, levels=levels_, pixels = 100)