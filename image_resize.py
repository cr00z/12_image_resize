from PIL import Image
import argparse
import os
import re


LAST_DOT_INDEX = 1


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='Simple console script for resize JPG and PNG images'
    )
    parser.add_argument(
        'input_path',
        metavar='path/to/original',
        help='path for input image'
    )
    parser.add_argument('--width', type=int, help='new width of image')
    parser.add_argument('--height', type=int, help='new height of image')
    parser.add_argument('--scale', type=float, help='new scale of image')
    parser.add_argument(
        '--output',
        metavar='path/to/result',
        help='path for output image'
    )
    return parser.parse_args()


def load_image(path_to_image):
    try:
        image = Image.open(path_to_image)
    except (OSError, IOError):
        image = None
    return image


def set_result_path(path_to_original, path_to_result, resolution_str):
    if path_to_result is None:
        result_file = os.path.split(path_to_original)[1]
        file_name, file_ext = result_file.rsplit('.', LAST_DOT_INDEX)
        result_path = '{}_{}.{}'.format(file_name, resolution_str, file_ext)
    else:
        if re.fullmatch(r'.*\.(jpg|jpeg|png)$', path_to_result, re.IGNORECASE):
            result_path = path_to_result
            result_dir = os.path.split(result_path)[0]
            if result_dir and not os.path.exists(result_dir):
                result_path = None
        else:
            result_path = None
    return result_path


def get_scales(new_scale, orig_width, orig_height, new_width, new_height):
    if new_scale and not new_width and not new_height:
        scale_x, scale_y = new_scale, new_scale
    elif not new_scale and (new_width or new_height):
        scale_x = new_width / orig_width if new_width else new_height / orig_height
        scale_y = new_height / orig_height if new_height else scale_x
    else:
        scale_x, scale_y = None, None
    return scale_x, scale_y


if __name__ == '__main__':
    args = get_cmdline_args()
    if not os.path.exists(args.input_path):
        exit('Image not found')
    orig_image = load_image(args.input_path)
    if orig_image is None:
        exit('File is not image')
    if args.scale is None and args.width is None and args.height is None:
        exit("Set 'scale' or 'width'/'height' parameters")

    orig_width, orig_height = orig_image.size
    scale_x, scale_y = get_scales(
        args.scale,
        orig_width,
        orig_height,
        args.width,
        args.height
    )
    if scale_x is None:
        exit("'Scale' and 'width'/'height' parameters cannot be used together")
    if scale_x != scale_y:
        print('Image aspect ratio is not remains the same!')
    new_width = int(orig_width * scale_x)
    new_height = int(orig_height * scale_y)

    resolution_str = '{}x{}'.format(new_width, new_height)
    result_path = set_result_path(args.input_path, args.output, resolution_str)
    if result_path is None:
        exit('Result directory not found OR result file must be jpg or png')
    resized_image = orig_image.resize((new_width, new_height))
    resized_image.save(result_path)
