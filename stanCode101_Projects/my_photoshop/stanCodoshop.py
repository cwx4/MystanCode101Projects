"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

This program remove the unexpected object in the photo.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2) ** 0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for pix in pixels:
        sum_red += pix.red
        sum_green += pix.green
        sum_blue += pix.blue

    red = sum_red//len(pixels)
    green = sum_green//len(pixels)
    blue = sum_blue//len(pixels)
    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for pix in pixels:
        sum_red += pix.red
        sum_green += pix.green
        sum_blue += pix.blue
    red = sum_red//len(pixels)
    green = sum_green//len(pixels)
    blue = sum_blue//len(pixels)

    best = 0
    best_pixel = 0

    for pixel in pixels:

        dist = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2) ** 0.5

        # pix_avg = (pixel.red + pixel.green + pixel.blue)/3
        if best == 0:
            best = dist
            best_pixel = pixel
        else:
            if dist < best:
                # abs(pix_avg-dist) < best:  ---> ghost
                # abs(pix_avg-dist) > best:  ---> shoe
                best = dist
                best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            pixels = []
            for img in images:
                pixel = img.get_pixel(x, y)
                pixels.append(pixel)
            best_pixel = get_best_pixel(pixels)

            result_pix = result.get_pixel(x, y)

            result_pix.red = best_pixel.red
            result_pix.green = best_pixel.green
            result_pix.blue = best_pixel.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        image.show()
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
