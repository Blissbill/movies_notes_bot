from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from bot.settings import settings

__engine = create_engine(settings.database_url, echo=False)
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=__engine, expire_on_commit=False))


class CRUDMixin(object):
    query = session.query_property()

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        session.add(self)
        if commit:
            session.commit()
        return self

    def delete(self, commit=True):
        session.delete(self)
        return commit and session.commit()


Base = declarative_base(cls=CRUDMixin)


class Model(Base):
    __abstract__ = True
