from datetime import datetime

import sqlalchemy as sa

from bot.database import Model


class User(Model):
    __tablename__ = "user_user"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, nullable=True)
    first_name = sa.Column(sa.String, nullable=True)
    last_name = sa.Column(sa.String, nullable=True)
    telegram_id = sa.Column(sa.Integer)
    is_active = sa.Column(sa.Boolean, default=True)
    date_joined = sa.Column(sa.DateTime, default=datetime.utcnow)
    is_superuser = sa.Column(sa.Boolean, default=False)

