#!/usr/bin/env python3

"""
This module provides a `DB` class for interacting with a database
using Object-Relational Mapping (ORM).
"""

from sqlalchemy import create_engin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import Dict

from user import Base
from user import User


class DB:
    """
    Represents a database connection and provides methods for interacting
    with user data in the 'users' table.
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

    def find_user_by(self, kwargs: Dict[str, str]) -> User:
        """
        Finds a user based on a dictionary of search criteria
        matching user table columns.

        Args:
            kwargs (Dict[str, str]): A dictionary containing key-value pairs
                where the key represents the user attribute and the value
                represents the search value.

        Returns:
            User: The first user matching the provided criteria.

        Raises:
            InvalidRequestError: If no search criteria are provided.
            ValueError: If an invalid search criterion is provided (not a user table column).
            NoResultFound: If no user is found matching the criteria.
        """
        if not kwargs:
            raise InvalidRequestError("No search criteria provided.")

        valid_keys = {"id", "email", "hashed_password", "session_id", "reset_token"}
        for key in kwargs.keys():
            if key not in valid_keys:
                raise ValueError(f"Invalid search criteria: {key}")

        user = self.session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found matching the criteria.")

        return user

    def update_user(self, user_id: int, kwargs: Dict[str, str]) -> None:
        """
        Updates a user's attributes based on the provided user ID and a dictionary
        of key-value pairs representing the updates.

        Args:
            user_id (int): The ID of the user to update.
            kwargs (Dict[str, str]): A dictionary containing key-value pairs
                where the key represents the user attribute to update and the value
                represents the new value.

        Raises:
            ValueError: If an invalid update criterion is provided (not a user table column).
        """
        user_to_update = self.find_user_by(id=user_id)

        valid_keys = {"id", "email", "hashed_password", "session_id", "reset_token"}
        for key, value in kwargs.items():
            if key not in valid_keys:
                raise ValueError(f"Invalid update criteria: {key}")

            setattr(user_to_update, key, value)

        self.session.commit()
