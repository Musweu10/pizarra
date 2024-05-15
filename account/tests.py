from django.test import TestCase

# Create your tests here.
import pytest
from django.contrib.auth.models import User
from django.contrib.auth.models import create_user


@pytest.mark.django_db
def test_create_user():
    user = create_user(email="<EMAIL>", password="password")
    assert user.email == "<EMAIL>"
    assert user.check_password("password")