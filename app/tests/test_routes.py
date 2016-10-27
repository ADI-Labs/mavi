import pytest
import html_linter


@pytest.mark.parametrize("url", ["/", "/post", "/about"])
def test_html_style(app, url):
    response = app.get(url)
    assert response.status_code == 200
    assert response.mimetype == "text/html"
