import pathlib
from datetime import datetime
import logging

logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

logging.basicConfig(
    filename= logs_dir / f"log_{timestamp}.log",
    level=logging.INFO,
    format= "%(asctime)s %(levelname)s %(name)s - %(message)s",
    force=True
)

logger = logging.getLogger("talento_tech")
