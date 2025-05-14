
import pytest
import pickle
from utils.hash_utils import get_pickle_hash

# 测试数据样本
test_objects = {
    "整数": 42,
    "浮点数": 3.14159,
    "布尔值": True,
    "字符串": "ChatGPT",
    "列表": [1, 2, 3],
    "字典": {"a": 1, "b": 2},
    "元组": (4, 5, 6),
    "集合": {7, 8, 9},
    "嵌套结构": {"x": [1, {"y": (3, 4)}]},
    "空值": None
}

@pytest.mark.parametrize("name,obj", test_objects.items())
def test_pickle_hash_stability(name, obj):
    """测试 pickle 同一个对象的 hash 是否一致"""
    hash1 = get_pickle_hash(obj)
    hash2 = get_pickle_hash(obj)
    hash3 = get_pickle_hash(obj)
    assert hash1 == hash2 == hash3, f"对象 '{name}' 的 hash 不一致！"

