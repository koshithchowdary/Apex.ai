from core.memory import Memory
def test_round_trip(tmp_path):
    m=Memory(str(tmp_path/"m.db")); m.add("user","hello"); m.add("assistant","hi")
    assert m.recent(2)==[("user","hello"),("assistant","hi")]
def test_clear(tmp_path):
    m=Memory(str(tmp_path/"m.db")); m.add("user","x"); m.clear(); assert m.recent()==[]
