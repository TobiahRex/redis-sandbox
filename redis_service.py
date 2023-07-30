import redis

class RedisService:
    def __init__(self, host='localhost', port=6379, password=None, db=0):
        """
        Initialize the RedisService class with connection parameters.

        :param host: Redis server hostname (default is 'localhost')
        :param port: Redis server port (default is 6379)
        :param password: Redis server password (default is None)
        :param db: Redis database number (default is 0)
        """
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.redis_client = None

    def connect(self):
        """
        Connect to the Redis server using the provided connection parameters.
        """
        try:
            self.redis_client = redis.StrictRedis(
                host=self.host, port=self.port, password=self.password, db=self.db, decode_responses=True
            )
            # 'decode_responses=True' allows the returned values to be in string format instead of bytes.
            self.redis_client.ping()  # Test the connection
            print("Connected to Redis server.")
        except redis.exceptions.ConnectionError as e:
            raise Exception(f"Error connecting to Redis server: {e}")

    def set(self, key, value):
        """
        Set a key-value pair in the Redis server.

        :param key: The key to set
        :param value: The value to set for the key
        :return: True if the key was set successfully, False otherwise
        """
        if not self.redis_client:
            raise Exception("Redis client is not connected. Call connect() first.")

        return self.redis_client.set(key, value)

    def get(self, key):
        """
        Get the value of a key from the Redis server.

        :param key: The key to retrieve
        :return: The value associated with the key (None if key not found)
        """
        if not self.redis_client:
            raise Exception("Redis client is not connected. Call connect() first.")

        return self.redis_client.get(key)

    def delete(self, key):
        """
        Delete a key from the Redis server.

        :param key: The key to delete
        :return: True if the key was deleted successfully, False otherwise
        """
        if not self.redis_client:
            raise Exception("Redis client is not connected. Call connect() first.")

        return self.redis_client.delete(key)
