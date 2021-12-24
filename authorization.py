import tekore as tk

#to authorize your access to the Spotify API and return an object that allows you to access the API
def authorize():
 CLIENT_ID = “b5b113246ffa4a1596967853687e29e0”
 CLIENT_SECRET = “de4430468d044baf81f7dc3eefed6771”
 app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
 return tk.Spotify(app_token)