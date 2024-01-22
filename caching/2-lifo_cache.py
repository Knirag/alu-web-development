#!/usr/bin/python3
"""
LIFO module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines an LIFO algorithm for caching.
    """

    def __init__(self):
        """ Initialize the cache.
        """
        super().__init__()
        self.least_recent = []

    def put(self, key, item):
        """
        Modify cache data.

        Args:
            key: Key for the cache.
            item: Value associated with the key.
        """
        if key or item is not None:
            value_cache = self.get(key)
            # Make a new entry if key doesn't exist
            if value_cache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keys_to_discard = self.least_recent
                    last_key_index = len(keys_to_discard) - 1
                    key_to_discard = keys_to_discard[last_key_index]
                    del self.cache_data[key_to_discard]
                    print("DISCARD: {}".format(keys_to_discard[last_key_index]))
            else:
                del self.cache_data[key]

            if key in self.least_recent:
                self.least_recent.remove(key)
                self.least_recent.append(key)
            else:
                self.least_recent.append(key)

            self.cache_data[key] = item

    def get(self, key):
        """
        Modify cache data.

        Args:
            key: Key for the cache.

        Return:
            Value associated with the key.
        """
        value_cache = self.cache_data.get(key)

        if value_cache:
            self.least_recent.remove(key)
            self.least_recent.append(key)

        return value_cache
