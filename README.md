# tinyfeet
Saw that an external form-filling procedure could be speeded up.
Tested how quickly this can be done.

Created a memcache with this in git bash -
heroku addons:create memcachier:dev --app resoler

heroku config
allows us to see the memcache pwd, servers and username
we can then amend our config file to gather these
