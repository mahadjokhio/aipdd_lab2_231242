"""DataIngestion: pulls frames from a camera, RTSP stream, or video file."""

from typing import Optional

from datatypes import Frame


class DataIngestion:
    """Owns the connection to the video source and hands out decoded frames.

    Responsibilities:
        - open / close the source (RTSP URL, device index, or file path)
        - drop frames to hold the target FPS
        - reconnect when the stream drops
    """

    def __init__(self, source_uri: str, source_id: str = "cam-01",
                 target_fps: int = 15, max_reconnect_attempts: int = 5) -> None:
        raise NotImplementedError

    def connect(self) -> bool:
        """Open the video source. Returns True on success."""
        raise NotImplementedError

    def read_frame(self) -> Optional[Frame]:
        """Return the next frame, or None if the source is closed or a read failed."""
        raise NotImplementedError

    def is_connected(self) -> bool:
        """True while the source is open and delivering frames."""
        raise NotImplementedError

    def reconnect(self) -> bool:
        """Retry the connection up to max_reconnect_attempts. Returns True on success."""
        raise NotImplementedError

    def release(self) -> None:
        """Close the source and free resources."""
        raise NotImplementedError
