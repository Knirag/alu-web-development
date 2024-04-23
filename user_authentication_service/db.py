#!/usr/bin/env python3

"""
This file defines a `DB` class for interacting with a database
using Object-Relational Mapping (ORM).
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from typing import TypeVar

from user import Base
from user import User


class DB:
    """
    Represents a database connection and provides methods for interacting
    with user data using SQLAlchemy ORM.
    """

    def __init__(self):
        """
        Initializes the database connection and creates all tables
        if they don't already exist.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def session(self):
        """
        Returns a database session object for interacting with data.
        Creates a new session if one doesn't already exist.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The newly created user object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self.session.add(user)
        self.session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user based on keyword arguments matching user table columns.

        Args:
            **kwargs: Keyword arguments representing user attributes (e.g., id=1, email="user@example.com").

        Returns:
            User: The first user matching the provided criteria.

        Raises:
            InvalidRequestError: If no keyword arguments are provided.
            ValueError: If an invalid keyword argument is provided (not a user table column).
            NoResultFound: If no user is found matching the criteria.
        """
        if not kwargs:
            raise InvalidRequestError("No search criteria provided.")

        for key in kwargs.keys():
            if key not in User.__table__.columns.keys():
                raise ValueError(f"Invalid search criteria: {key}")

        user = self.session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found matching the criteria.")

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates a user's attributes based on the provided user ID and keyword arguments.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Keyword arguments representing user attributes to update (e.g., email="new_email@example.com").

        Raises:
            ValueError: If an invalid keyword argument is provided (not a user table column).
        """
        user = self.find_user_by(id=user_id)

        for key in kwargs.keys():
            if key not in User.__table__.columns.keys():
                raise ValueError(f"Invalid update criteria: {key}")

        for key, value in kwargs.items():
            setattr(user, key, value)

        self.session.commit()
