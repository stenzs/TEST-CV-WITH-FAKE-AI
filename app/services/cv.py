import base64
import numpy
import cv2
HEIGHT, WIDTH = 640, 640


def transform_image(file):
    try:
        image_array = numpy.frombuffer(file.file.read(), numpy.uint8)
        image = cv2.imdecode(image_array, -1)
        resized_image = cv2.resize(image, (HEIGHT, WIDTH))
        normalized_image = cv2.normalize(resized_image, None, alpha=0, beta=200, norm_type=cv2.NORM_MINMAX)
        res, buffer = cv2.imencode(".png", normalized_image)
        image_string = base64.b64encode(buffer).decode("utf-8")

    except Exception:
        return None
    return image_string
