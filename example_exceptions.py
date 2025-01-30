try:
    raise ValueError("This is a value error")
except ValueError as e:
    print("Caught a ValueError")
    raise
except TypeError as e:
    ...
except IndexError as e:
    ...
finally:
    ...