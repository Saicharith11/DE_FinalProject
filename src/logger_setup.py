import logging
from pathlib import Path

from config import LOG_FOLDER


def setup_logger():
    """Create and return the project logger."""
    logs_folder = Path(LOG_FOLDER)
    logs_folder.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=logs_folder / "app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )
    return logging.getLogger(__name__)
