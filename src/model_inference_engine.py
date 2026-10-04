"""ModelInferenceEngine: loads the detector and returns detections."""

from typing import List

import numpy as np

from datatypes import Detection, PreprocessedFrame


class ModelInferenceEngine:
    """Wraps the object detection model.

    Responsibilities:
        - load weights once at startup
        - run the forward pass
        - filter by confidence, apply NMS, and map boxes back to the original frame
    """

    def __init__(self, model_path: str, class_names: List[str],
                 conf_threshold: float = 0.5, iou_threshold: float = 0.45,
                 device: str = "cpu") -> None:
        raise NotImplementedError

    def load_model(self) -> None:
        """Load weights from model_path onto the chosen device."""
        raise NotImplementedError

    def warmup(self, runs: int = 3) -> None:
        """Run a few dummy inferences so the first real frame isn't slow."""
        raise NotImplementedError

    def infer(self, pre: PreprocessedFrame) -> List[Detection]:
        """Run the model on one preprocessed frame and return final detections."""
        raise NotImplementedError

    def postprocess(self, raw_output: np.ndarray, pre: PreprocessedFrame) -> List[Detection]:
        """Confidence filter + NMS + rescale boxes to original-frame coordinates."""
        raise NotImplementedError
