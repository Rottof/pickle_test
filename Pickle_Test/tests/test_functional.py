import pytest
import pickle

test_data = {
    "整数": 123,
    "浮点数": 3.14,
    "布尔值": True,
    "字符串": "Hello, pickle!",
    "列表": [1, 2, 3],
    "字典": {"a": 1, "b": 2},
    "嵌套结构": {"x": [1, {"y": (3, 4)}]},
    "元组": (1, 2, 3),
    "集合": {5, 6, 7},
    "空值": None
}

@pytest.mark.parametrize("name,obj", test_data.items())
def test_pickle_functionality(name, obj):
    """测试 pickle 能否成功还原对象结构"""
    try:
        data = pickle.dumps(obj)
        result = pickle.loads(data)
        assert result == obj, f"{name} 反序列化结果不一致"
    except Exception as e:
        pytest.fail(f"{name} 测试失败: {e}")
