from PIL import Image


def resize_image(path_to_original, path_to_result):
    image = Image.open('photo.jpg')
    resized_image = image.resize((500, 500))
    resized_image.save('photo_500x500.jpg')
    pass


if __name__ == '__main__':
    resize_image('','')
