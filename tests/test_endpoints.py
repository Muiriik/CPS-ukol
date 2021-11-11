# check homepage
def test_index_status(client):
  response = client.get('/')
  statuscode = response.status_code
  assert statuscode == 200

def test_none_existend_page(client):
  response = client.get('/randompage')
  statuscode = response.status_code
  assert statuscode == 404

# check feed endpoints
def test_json_feed_status_post_request(client):
  response = client.post('/feed.json')
  statuscode = response.status_code
  assert statuscode == 405

def test_json_feed_status_get_request(client):
  response = client.get('/feed.json')
  statuscode = response.status_code
  assert statuscode == 200