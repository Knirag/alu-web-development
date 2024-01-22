#!/usr/bin/python3
"""
MRUCache 
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines an MRU algorithm for caching."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.most_recent = []

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
                    key_to_discard = self.most_recent.pop()
                    del self.cache_data[key_to_discard]
                    print("DISCARD: {}".format(key_to_discard))
            else:
                del self.cache_data[key]

            if key in self.most_recent:
                self.most_recent.remove(key)
                self.most_recent.append(key)
            else:
                self.most_recent.append(key)

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
            self.most_recent.remove(key)
            self.most_recent.append(key)

        return value_cache
