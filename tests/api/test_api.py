def test_get_post_returns_expected_data(api_context):
    response = api_context.get("/posts/1")
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"]


def test_create_post_returns_201(api_context):
    response = api_context.post(
        "/posts",
        data={"title": "Playwright API test", "body": "API + UI in one suite", "userId": 1},
    )
    assert response.status == 201
    assert response.json()["title"] == "Playwright API test"


def test_nonexistent_post_returns_404(api_context):
    # jsonplaceholder returns {} with 404 for a missing post id in this
    # style of API check; assert on status, not on a specific error body.
    response = api_context.get("/posts/999999")
    assert response.status == 404
