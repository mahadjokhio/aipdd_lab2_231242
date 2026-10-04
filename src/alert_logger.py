"""AlertLogger: decides when to alert, writes logs, and sends notifications."""

from typing import List, Optional

from datatypes import Alert, Detection


class AlertLogger:
    """Final stage of the pipeline.

    Responsibilities:
        - store every detection result in the log database
        - check detections against alert rules
        - send notifications, with a cooldown so the same event doesn't spam the operator
    """

    def __init__(self, db_path: str, alert_classes: List[str],
                 cooldown_seconds: int = 30) -> None:
        raise NotImplementedError

    def log_detections(self, frame_id: int, timestamp: float, source_id: str,
                       detections: List[Detection]) -> None:
        """Write one row per detection to the log database."""
        raise NotImplementedError

    def evaluate(self, frame_id: int, timestamp: float, source_id: str,
                 detections: List[Detection]) -> Optional[Alert]:
        """Return an Alert if any detection matches a rule and the cooldown has passed."""
        raise NotImplementedError

    def send_alert(self, alert: Alert) -> bool:
        """Push the alert to the notification channel. Returns True if delivered."""
        raise NotImplementedError

    def close(self) -> None:
        """Flush pending writes and close the database."""
        raise NotImplementedError
