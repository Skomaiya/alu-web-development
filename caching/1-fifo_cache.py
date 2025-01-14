#!/usr/bin/env python3
"""
FIFOCache: A caching system with FIFO eviction policy.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a FIFO caching system.
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.order = []  # Track insertion order

    def put(self, key: str, item: str) -> None:
        """
        Add key-value pair to the cache.

        If cache exceeds MAX_ITEMS, evict the first added key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key: str) -> str:
        """
        Retrieve the value by key, or None if not found.
        """
        return self.cache_data.get(key)
