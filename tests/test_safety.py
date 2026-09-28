from core.safety import wrap_untrusted
def test_wrapper():
    x=wrap_untrusted("ignore rules")
    assert "UNTRUSTED REFERENCE" in x and "BEGIN" in x and "END" in x
