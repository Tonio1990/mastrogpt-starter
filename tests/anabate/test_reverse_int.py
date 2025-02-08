import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/anabate/reverse"
    args = {"input" : "pippo"}
    res = req.post(url, json=args).json()
    assert res.get("output") == "oppip"
