from PIL import Image
import argparse


def resize_image(path_to_original, path_to_result):
    image = Image.open('photo.jpg')
    resized_image = image.resize((500, 500))
    resized_image.save('photo_500x500.jpg')
    pass


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='Simple console script for resize JPG and PNG images'
    )
    parser.add_argument(
        'input_path',
        metavar = "INPUT",
        help='path for input image')
    parser.add_argument(
        '--width',
        type=int,
        help='new width of image'
    )
    parser.add_argument(
        '--height',
        type=int,
        help='new height of image'
    )
    parser.add_argument(
        '--scale',
        type=float,
        help='new scale of image'
    )
    parser.add_argument(
        '--output',
        help='path for output image'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_cmdline_args()
    resize_image('','')
