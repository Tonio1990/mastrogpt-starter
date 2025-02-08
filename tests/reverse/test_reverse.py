import sys 
sys.path.append("packages/reverse/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({'input': "Test"})
    assert res["output"] == "tseT"
