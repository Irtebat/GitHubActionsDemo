import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    ISSUE_URL = os.environ["ISSUE_URL"]
except KeyError:
    ISSUE_URL = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f'New Issue Added at {ISSUE_URL}')

    # token = os.environ["PERSONAL_TOKEN"]
    # headers = {'Authorization': f'token {token}'}
    # repoIssueUrl=f"https://api.github.com/repos/Irtebat/GitHubActionsDemo/issues/1/comments"

    # r = requests.get(repoIssueUrl, headers=headers)

    # if r.status_code == 200:
    #     data = r.json()
    #     logger.info(f'New Issue Added at {ISSUE_URL}')