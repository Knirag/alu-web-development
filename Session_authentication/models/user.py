#!/usr/bin/env python3
""" User module containing the User class.

This module defines a User class that inherits from the Base class. The User class
represents user objects with attributes such as 'email', '_password', 'first_name',
and 'last_name'. It includes methods for password management, password validation,
and generating a display name.

Attributes:
    hashlib: A module providing hash functions.
    Base: The base class for object representation.
"""

import hashlib
from models.base import Base

class User(Base):
    """ User class representing user objects.

    Attributes:
        email (str): Email address associated with the user.
        _password (str): Encrypted password using SHA256.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a User instance with default or provided values.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    @property
    def password(self) -> str:
        """ Getter of the password
        """
        return self._password

    @password.setter
    def password(self, pwd: str):
        """ Setter of a new password: encrypt in SHA256
        """
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd: str) -> bool:
        """ Validate a password
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        pwd_e = pwd.encode()
        return hashlib.sha256(pwd_e).hexdigest().lower() == self.password

    def display_name(self) -> str:
        """ Display User name based on email/first_name/last_name
        """
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)
