Author: Shck Tchamna (Tchamna@gmail.com)

This script, created by Shck Tchamna (Tchamna@gmail.com), allows you to randomly sample parts of images based on the percentage of their width and height. 
This script will iterate through a folder where images are placed, then randomly sample parts of the images at different points, based on the percentage of the width and height


HOW TO USE THE CODE?

By following the instructions below, you can quickly and easily extract samples from a folder of images:

1. Copy the entire "GetSampleImages" folder to a directory and unzip it if necessary.
2. Place the images you want to extract samples from in the "Original_Images" folder.
3. Double-click the "get_sample_images.bat" batch script to run the code.
4. The resulting samples will be saved in the "Resulting_Samples" folder.

For advanced users, there are options to modify the crop level and the dimensions of the cropped samples. 
By adjusting the levels_ variable and the pixels parameter in the take_samples() function, you can tailor the script to your needs.

By default, the croped size of the picture is 100 x 100 Pixels and the sample level is 2. It cropped at 25% and 90% of the width and height

If you want to modify the crop level

# crop at 25% (width, height)  50% (width, height) and at 90% (width, height) 
levels_ = [0.25, 0.5, 0.9] 
 # crop at 25% (width, height) and at 90% (width, height) 
levels_ = [0.25, 0.9]

If you want to change the dimension of the cropped sample, and/or change the "pixels" parameter, go to the last line of the python script and change the values of those parameters in the function "take_samples()" 
take_samples(image_path, levels=levels_, pixels = 100):

Example
pixels = 100: Crop 100x100 pixels
pixels = 200: Crop 200x200 pixels

Please note that this script might require python and the PIL library to be installed in order to work.


Thank you for using the GetSampleImages script!

Shck Tchamna
