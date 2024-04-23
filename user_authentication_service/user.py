#!/usr/bin/env python3

"""
This file defines a User model for a database table named 'users'.

The User model represents a user in the system and stores relevant information
such as email, hashed password (for security), session ID (for maintaining sessions),
and reset token (for password resets).
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    The User model represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user (primary key).
        email (str): The user's email address (unique and non-nullable).
        hashed_password (str): The hashed password for the user (nullable).
        session_id (str): The user's session identifier (nullable).
        reset_token (str): A token used for password resets (nullable).
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

