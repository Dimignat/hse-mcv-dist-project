"""
Main script. Runs image processing
"""

import os
from typing import Optional

import cv2
import numpy as np

try:
    from tflite_runtime.interpreter import Interpreter
except ImportError:
    from tensorflow.lite.python.interpreter import Interpreter


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(THIS_DIR, "gosling.jpeg")
MODEL_PATH = os.path.join(THIS_DIR, "model_float16_quant.tflite")


def process_image(
    img: np.ndarray, show: bool = True
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Run image processing.
    :param img: image to process.
    :param show: whether to display images.
    :return: Tuple of three processed images.
    """
    if show:
        cv2.imshow("source", img)
        cv2.waitKey(0)

    h = img.shape[0]
    w = img.shape[1]

    img = cv2.resize(img, (128, 128))
    img = np.asarray(img)
    img = img / 255.0
    img = img.astype(np.float32)
    img = img[np.newaxis, :, :, :]

    # Tensorflow Lite
    interpreter = Interpreter(model_path=MODEL_PATH, num_threads=4)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()[0]["index"]
    output_details = interpreter.get_output_details()[0]["index"]

    interpreter.set_tensor(input_details, img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details)

    out1 = output[0][:, :, 0]
    out2 = output[0][:, :, 1]

    out1 = np.invert((out1 > 0.5) * 255)
    out2 = np.invert((out2 > 0.5) * 255)

    out1 = cv2.resize(np.uint8(out1), (w, h))
    if show:
        cv2.imshow("out1", out1)
        cv2.waitKey(0)

    out2 = cv2.resize(np.uint8(out2), (w, h))
    if show:
        cv2.imshow("out2", out2)
        cv2.waitKey(0)

    out3 = cv2.ximgproc.jointBilateralFilter(out2, out1, 8, 75, 75)
    if show:
        cv2.imshow("out3", out3)
        cv2.waitKey(0)

    if show:
        cv2.destroyAllWindows()

    return out1, out2, out3


def main(
    img_size: Optional[tuple[int, int]] = None, show: bool = True
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Run predefined image processing.
    :param img_size: new image size. Must be less than original.
    :param show: whether to display images.
    :return:
    """
    img = cv2.imread(IMG_PATH)
    if img_size is not None:
        img = cv2.resize(img, img_size, interpolation=cv2.INTER_AREA)
    return process_image(img, show=show)


if __name__ == "__main__":
    main()
