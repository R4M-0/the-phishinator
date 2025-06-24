from src.predict import predict_url

def test_legitimate():
    assert predict_url("https://www.google.com") == "Legitimate"

def test_phishing():
    assert predict_url("http://secure-login-update-paypal.com") == "Phishing"
