import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_page_returns_200(client):
    url = reverse("portfolio:home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_page_uses_correct_template(client):
    url = reverse("portfolio:home")
    response = client.get(url)
    assert "portfolio/home.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_health_check_returns_200(client):
    url = reverse("health-check")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_health_check_returns_json(client):
    url = reverse("health-check")
    response = client.get(url)
    assert response.json() == {"status": "ok"}


@pytest.mark.django_db
def test_home_page_has_featured_mixes_context(client):
    url = reverse("portfolio:home")
    response = client.get(url)
    assert "featured_mixes" in response.context


@pytest.mark.django_db
def test_home_page_has_upcoming_events_context(client):
    url = reverse("portfolio:home")
    response = client.get(url)
    assert "upcoming_events" in response.context
