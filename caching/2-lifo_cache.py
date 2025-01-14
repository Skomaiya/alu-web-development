#!/usr/bin/env python3
"""
LIFOCache: A caching system with LIFO eviction policy.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements a LIFO caching system.
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.last_key = None  # Track the most recently added key

    def put(self, key: str, item: str) -> None:
        """
        Add key-value pair to the cache.

        Evict the last added key if cache exceeds MAX_ITEMS.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key in self.cache_data:
            self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.last_key
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
            self.last_key = key

    def get(self, key: str) -> str:
        """
        Retrieve the value by key, or None if not found.
        """
        return self.cache_data.get(key)
