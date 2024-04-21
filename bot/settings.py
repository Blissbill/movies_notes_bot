import logging.config
import os.path
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_dir: Path = Path(__file__).parents[1]

    bot_token: str = SettingsConfigDict()
    logging: dict = {
        'version': 1,
        'formatters': {
            'console': {
                'format': '%(name)s\t[%(funcName)s:%(lineno)s]\t%(asctime)s\t[%(levelname)s]\t%(message)s',
                'datefmt': "%Y-%m-%d %H:%M:%S",
            }
        },
        'handlers': {
            'null': {
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'filters': [],
                'class': 'logging.StreamHandler',
                'formatter': 'console',
            },
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'DEBUG'
            },
        }
    }
    messages_file: Path = os.path.join(base_dir, "messages.json")


settings = Settings(_env_file='.env', _env_file_encoding='utf-8', _case_sensitive=False)
logging.config.dictConfig(settings.logging)
