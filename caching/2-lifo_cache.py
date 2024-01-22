#!/usr/bin/python3
""" 3-main """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a LIFO algorithm for caching."""

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
            # Make a new entry if key doesn't exist
            if value_cache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keys_to_discard = list(self.cache_data.keys())
                    last_key_index = len(keys_to_discard) - 1
                    del self.cache_data[keys_to_discard[last_key_index]]
                    print("DISCARD: {}".format(keys_to_discard[last_key_index]))
            # If the key already exists, delete it before updating
            else:
                del self.cache_data[key]
            # Modify value
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
