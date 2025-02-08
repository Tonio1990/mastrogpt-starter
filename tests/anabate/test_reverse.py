import sys 
sys.path.append("packages/anabate/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({"input": "pippo"})
    assert res["output"] == "oppip"
