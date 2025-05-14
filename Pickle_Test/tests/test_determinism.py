import pickle
import hashlib


def test_pickle_is_deterministic():
    obj = {"a": 1, "b": 2}  # 测试用例对象（字典）

    # 使用 pickle.dumps 两次序列化相同对象
    pkl1 = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    pkl2 = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)

    # 计算序列化结果的哈希值（使用 SHA-256）
    hash1 = hashlib.sha256(pkl1).hexdigest()
    hash2 = hashlib.sha256(pkl2).hexdigest()

    # 断言：两次序列化结果的哈希应相同
    assert hash1 == hash2, f"Hashes differ: {hash1} != {hash2}"
