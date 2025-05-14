import pickle
import hashlib

def get_pickle_hash(obj, protocol=pickle.DEFAULT_PROTOCOL):
    try:
        data = pickle.dumps(obj, protocol=protocol)
        return hashlib.sha256(data).hexdigest()
    except Exception as e:
        return f"ERROR: {e}"
