#!/usr/bin/env python3
"""
BasicCache module implementing a basic caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    Implements a caching system with no size limit.
    """

    def put(self, key: str, item: str) -> None:
        """
        Add an item to the cache.

        Args:
            key (str): The key associated with the item.
            item (str): The item to cache.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """
        Retrieve an item by key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            str: The value associated with the key, or None if the key is invalid
            or doesn't exist in the cache.
        """
        return self.cache_data.get(key)
