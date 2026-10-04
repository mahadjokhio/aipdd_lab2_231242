"""ImagePreprocessor: turns raw frames into model-ready tensors."""

from typing import Tuple

import numpy as np

from datatypes import Frame, PreprocessedFrame


class ImagePreprocessor:
    """Resize, pad, and normalize frames to match what the model expects."""

    def __init__(self, input_size: Tuple[int, int] = (640, 640),
                 normalize: bool = True, bgr_to_rgb: bool = True) -> None:
        raise NotImplementedError

    def process(self, frame: Frame) -> PreprocessedFrame:
        """Full preprocessing chain for one frame."""
        raise NotImplementedError

    def letterbox(self, image: np.ndarray) -> Tuple[np.ndarray, float, Tuple[int, int]]:
        """Resize keeping aspect ratio and pad to input_size.

        Returns (padded_image, scale, (pad_x, pad_y)).
        """
        raise NotImplementedError

    def normalize_image(self, image: np.ndarray) -> np.ndarray:
        """Scale pixel values to [0, 1] and reorder to 1 x C x H x W float32."""
        raise NotImplementedError
