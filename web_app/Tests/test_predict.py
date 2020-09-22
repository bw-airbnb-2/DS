from fastapi.testclient import testclient

from app.main import app

client = testclient(app)


def test_valid_input():

    """ Return 200 Success when input is valid """

def test_invalid_input():
    """ Return 422 Validation Error when x1 is negative """