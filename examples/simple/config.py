from huey import RedisHuey, SqliteHuey

# huey = RedisHuey('simple.test', blocking=True)
huey = SqliteHuey()
