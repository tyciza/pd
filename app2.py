
def normalize_data(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        min_val, max_val = min(data), max(data)
        normalized = [(x - min_val) / (max_val - min_val) for x in data]
        print("Dane po normalizacji:", normalized)
        return normalized
    return wrapper

@normalize_data
def get_data():
    return [10, 15, 20, 30, 50]

get_data()
