"""Shared data containers passed between pipeline modules."""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import numpy as np


@dataclass
class Frame:
    """A single decoded video frame."""
    frame_id: int
    timestamp: float          # Unix time, seconds
    image: np.ndarray         # H x W x 3, BGR, uint8
    source_id: str            # camera / stream identifier


@dataclass
class PreprocessedFrame:
    """Model-ready tensor plus the info needed to map boxes back to the original frame."""
    frame_id: int
    tensor: np.ndarray        # 1 x 3 x H x W, float32, normalized
    scale: float              # resize ratio applied to the original frame
    pad: Tuple[int, int]      # (pad_x, pad_y) added by letterboxing
    original_size: Tuple[int, int]  # (width, height)


@dataclass
class Detection:
    """One detected object, in original-frame pixel coordinates."""
    label: str
    confidence: float
    bbox: Tuple[int, int, int, int]  # x1, y1, x2, y2


@dataclass
class Alert:
    """Raised when detections match an alert rule."""
    frame_id: int
    timestamp: float
    source_id: str
    reason: str
    detections: List[Detection] = field(default_factory=list)
    meta: Dict[str, str] = field(default_factory=dict)
