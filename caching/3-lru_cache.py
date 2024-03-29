#!/usr/bin/python3
"""
BaseCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines an LRU algorithm for caching."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.least_recent = []

    def put(self, key, item):
        """
        Modify cache data.

        Args:
            key: Key for the cache.
            item: Value associated with the key.
        """
        if key is not None and item is not None:
            value_cache = self.get(key)
            # Make a new entry if key doesn't exist
            if value_cache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    key_to_discard = self.least_recent.pop()
                    del self.cache_data[key_to_discard]
                    print("DISCARD: {}".format(key_to_discard))
            else:
                del self.cache_data[key]

            if key in self.least_recent:
                self.least_recent.remove(key)
                self.least_recent.insert(0, key)
            else:
                self.least_recent.insert(0, key)

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
            self.least_recent.insert(0, key)

        return value_cache
