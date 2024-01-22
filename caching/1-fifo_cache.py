#!/usr/bin/env python3
""" 1-main """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a FIFO algorithm for caching."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()

    def put(self, key, item):
        """
        Modify cache data.

        Args:
            key: Key for the cache.
            item: Value associated with the key.
        """
        if key or item is not None:
            value_cache = self.get(key)
            if value_cache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    key_to_discard = list(self.cache_data.keys())[0]
                    del self.cache_data[key_to_discard]
                    print("DISCARD: {}".format(key_to_discard))

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
        return value_cache
