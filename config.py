from loguru._logger import Core as _Core
from loguru._logger import Logger
import os

LOG_PATH = "/log"


def add_logger(logger_name: str, script_name: str):
    logger_name = Logger(
        core=_Core(),
        exception=None,
        depth=0,
        record=False,
        lazy=False,
        colors=False,
        raw=False,
        capture=True,
        patcher=None,
        extra={},
    )

    logger_name.add(f"{LOG_PATH}/{script_name}.log", level="DEBUG", rotation="9:00")
    return logger_name


script_name = os.path.splitext(os.path.basename(__file__))[0]
logger = add_logger(f'logger_{script_name}', script_name)


def is_point_in_path(x: float, y: float, poly) -> bool:
    try:
        num = len(poly)
        j = num - 1
        c = False
        for i in range(num):
            if (x == poly[i][0]) and (y == poly[i][1]):
                return True
            if ((poly[i][1] > y) != (poly[j][1] > y)):
                slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (poly[j][0] - poly[i][0]) * (y - poly[i][1])
                if slope == 0:
                    return True
                if (slope < 0) != (poly[j][1] < poly[i][1]):
                    c = not c
            j = i
        return c

    except Exception as e:
        logger.info(f"An error occurred: {e}")
        return False
