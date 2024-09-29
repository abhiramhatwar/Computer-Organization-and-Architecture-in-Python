class CacheMemory:
    def __init__(self, size):
        self.cache = [None] * size
        self.size = size

    def access_memory(self, address):
        if address in self.cache:
            return f"Cache Hit: {address}"
        else:
            self.cache[address % self.size] = address
            return f"Cache Miss: {address}"

cache = CacheMemory(4)
print(cache.access_memory(5))
print(cache.access_memory(9))
print(cache.access_memory(5))
