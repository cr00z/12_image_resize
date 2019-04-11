# Image Resizer

Image Resizer is a simple console script for resize JPG and PNG images.

You may increase or decrease resolution of result image by:

* new width OR height - image aspect ratio is remains the same;
* new width AND height - image aspect ratio is not remains the same;
* new scale (less than 1 for zoom out, more than 1 for zoom in).

# How to Install

Python 3 should be already installed. 

Script use [Pillow](https://pypi.python.org/pypi/Pillow/3.3.1). Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python image_resize.py --scale 2 pic__100x200.jpg

$ ls
image_resize.py
pic__100x200.jpg
pic__100x200__200x400.jpg   <--- resized image

```

Use in Windows similarly.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
