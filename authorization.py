import tekore as tk

#to authorize your access to the Spotify API and return an object that allows you to access the API
def authorize():
 CLIENT_ID = βb5b113246ffa4a1596967853687e29e0β
 CLIENT_SECRET = βde4430468d044baf81f7dc3eefed6771β
 app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
 return tk.Spotify(app_token)