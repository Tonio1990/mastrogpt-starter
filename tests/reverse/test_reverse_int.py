import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/reverse/reverse"
    args = {"input": "Test"}
    res = req.post(url, json=args).json()
    assert res["output"] == 'tseT'
